from converters import transcribe, available_transriptions, transcribe_horizontal
from tqdm import tqdm
import argparse, json, os


def main():
    parser = argparse.ArgumentParser(
        prog='transcribe',
        description='Transcribes PAN20 datasets into phonetic transcriptions',
        add_help=True)
    parser.add_argument('-i', '--input', type=str, help='Path to a PAN20 dataset file (.jsonl)')
    args = parser.parse_args()
    if not args.input:
        print('ERROR: The input file is required')
        parser.exit(1)

    # Input: PAN20 file (relative path given)
    # Ouput: Transcribed PAN20 files in data/transcribed/
    transcription_systems = available_transriptions()
    print(f'Transcribing to {len(transcription_systems)} systems:')
    print(transcription_systems)

    os.makedirs(os.path.dirname('data/'), exist_ok=True)
    os.makedirs(os.path.dirname(os.path.join('data', 'transcribed/')), exist_ok=True)

    orig_entities = []
    with open(args.input, 'r') as f:
        for line in f:
            entity = json.loads(line)
            # entity: id (string), fandoms (list of strings), pair (list of strings, size 2?)
            orig_entities.append(entity)

    for entity in tqdm(orig_entities):
        copy = entity.copy()
        first_transcriptions = transcribe_horizontal(entity['pair'][0])
        second_transcriptions = transcribe_horizontal(entity['pair'][1])
        for system in transcription_systems:
            copy['pair'] = [first_transcriptions[system], second_transcriptions[system]]
            with open(os.path.join('data', 'transcribed', f'{system}_{os.path.basename(args.input)}'), 'w') as f:
                json.dump(copy, f, ensure_ascii=False)
                f.write('\n')



    # for i, system in enumerate(transcription_systems):
    #     transcribed_entities = []
    #     print(f'Transcribing to {system} ({i}/{len(transcription_systems)}).')
    #     for entity in tqdm(orig_entities):
    #         copy = entity.copy()
    #         first_transcribed = transcribe(entity['pair'][0], system)
    #         second_transcribed = transcribe(entity['pair'][1], system)
    #         copy['pair'] = [first_transcribed, second_transcribed]
    #         transcribed_entities.append(copy)
    #     with open(os.path.join('data', 'transcribed', f'{system}_{os.path.basename(args.input)}'), 'w') as f:
    #         for te in transcribed_entities:
    #             json.dump(te, f)
    #             f.write('\n')
            
        

if __name__ == '__main__':
    main()

