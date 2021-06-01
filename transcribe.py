from converters import transcribe
from tqdm import tqdm


def main():
    parser = argparse.ArgumentParser(
        prog='transcribe',
        description='Transcribes PAN20 datasets into phonetic transcriptions',
        add_help=True)

    parser.add_argument('-i', '--input' type=str, help='Path to a PAN20 dataset file')

if __name__ == '__main__':
    main()

# Input: PAN20 file (relative path given)
# Ouput: Transcribed PAN20 files in data/transcribed/