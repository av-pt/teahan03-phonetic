import argparse
import json
import os
import logging
import traceback
import time
import shutil

from tqdm import tqdm

from converters import available_transcriptions, transcribe_horizontal


def now(): return time.strftime("%Y-%m-%d_%H-%M-%S")


def persist_jsonl(path, obj):
    with open(path, 'a+') as f:
        json.dump(obj, f)
        f.write('\n')


def main():
    parser = argparse.ArgumentParser(
        prog='transcribe',
        description='Transcribes PAN20 datasets into phonetic transcriptions',
        add_help=True)
    parser.add_argument('-i', '--input', type=str, help='Path to a PAN20 dataset file (.jsonl)')
    parser.add_argument('-t', '--truth', type=str, default='',
                        help='Path to the corresponding PAN20 truth file (.jsonl)')
    parser.add_argument('-o', '--output', type=str, default='', help='Name for an output folder')
    parser.add_argument('-s', '--separate_folders', action='store_true',
                        help='Create separate folders for output files, each containing a copy of the truth file')
    args = parser.parse_args()
    if not args.input:
        print('ERROR: The input file is required')
        parser.exit(1)
    output_folder = args.output
    if args.output == '':
        output_folder = os.path.join('data', f'transcibed_{now()}')
        os.makedirs(os.path.dirname('data/'), exist_ok=True)
        os.makedirs(os.path.dirname(os.path.join('data', 'transcribed/')), exist_ok=True)
    else:
        os.makedirs(output_folder, exist_ok=True)

    # Input: PAN20 file (relative path given)
    # Output: Transcribed PAN20 files in data/transcribed/
    transcription_systems = available_transcriptions()
    print(f'Transcribing to {len(transcription_systems)} systems:')
    print(transcription_systems)

    # Create subdirectories if chosen
    if args.separate_folders:
        for system in transcription_systems:
            os.makedirs(os.path.join(output_folder, system), exist_ok=True)
            shutil.copy(args.truth, os.path.join(output_folder, system))
        os.makedirs(os.path.join(output_folder, 'verbatim'), exist_ok=True)
        shutil.copy(args.truth, os.path.join(output_folder, 'verbatim'))



    orig_entities = []
    with open(args.input, 'r') as f:
        for line in f:
            entity = json.loads(line)
            # entity: id (string), fandoms (list of strings), pair (list of strings, size 2?)
            orig_entities.append(entity)
    for entity in tqdm(orig_entities):
        copy = entity.copy()

        try:
            first_transcriptions = transcribe_horizontal(entity['pair'][0])
            second_transcriptions = transcribe_horizontal(entity['pair'][1])
        except Exception as e:
            print(f"Sample ID: {entity['id']}")
            logging.error(traceback.format_exc())
            continue  # Skip persisting if exception occurs

        for system in transcription_systems:
            copy['pair'] = [first_transcriptions[system], second_transcriptions[system]]
            if args.separate_folders:
                persist_jsonl(os.path.join(output_folder, system, f'{system}_{os.path.basename(args.input)}'), copy)
            else:
                persist_jsonl(os.path.join(output_folder, f'{system}_{os.path.basename(args.input)}'), copy)

        if args.separate_folders:
            persist_jsonl(os.path.join(output_folder, 'verbatim', f'verbatim_{os.path.basename(args.input)}'), entity)
        else:
            persist_jsonl(os.path.join(output_folder, f'verbatim_{os.path.basename(args.input)}'), entity)


if __name__ == '__main__':
    main()
