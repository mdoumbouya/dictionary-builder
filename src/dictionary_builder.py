from pathlib import Path
import argparse
import csv
striped_chars = ',.;!?:"()'


def compute_word_frequency(text):
    word_count_dict = {}

    for word in text.split():
        if word not in word_count_dict:
            word_count_dict[word] = 0
        word_count_dict[word] += 1

    word_list = sorted(word_count_dict.items(), key=lambda t:t[1], reverse=True)

    with open(args.output_file, 'w') as of:
        writer = csv.DictWriter(of, fieldnames=['word', 'count'])
        for w, c in word_list:
            writer.writerow(
                {
                    'word': w,
                    'count': c
                }
            )



def main(args):
    text = Path(args.input_file).read_text()
    for c in striped_chars:
        text = text.replace(c, ' ')

    word_frequency = compute_word_frequency(text.lower())


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-file", required=True)
    parser.add_argument("--output-file", required=True)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args)