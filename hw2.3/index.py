# coding=utf-8

import os
import chardet
import json
import xml.etree.ElementTree


def get_news_files_directory(type):
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, 'data', type)


def get_file_list(dir):
    return os.listdir(dir)


def read_file(file_path):
    filename, extension = os.path.splitext(file_path)
    with open(file_path, 'rb') as file:
        data = file.read()
        encoding = chardet.detect(data)['encoding']
        data = data.decode(encoding)

        if extension == '.json':
            data = json.loads(data)
            data = [item['description'] for item in data['rss']['channel']['items']]
        elif extension == '.xml':
            e = xml.etree.ElementTree.fromstring(data)
            items = e.findall('./channel/item/description')
            data = [t.text for t in items]

        return data


def count_long_words(words):
    long_words = [w for w in words if len(w) > 6]
    word_numbers = {word: long_words.count(word) for word in long_words}
    return sorted(word_numbers.items(), key=lambda item: item[1], reverse=True)


def print_words(filename, words):
    print("Самые популярные слова в файле %s" % filename)
    for word, count in words:
        print("%s: %s" %(word, count))
    print()


def process_files(file_list):
    words = []
    for file in file_list:
        [words.extend(line[:-1].split(' ')) for line in read_file(file)]
        sorted_word_numbers = count_long_words(words)
        filtered_words = [word for word in sorted_word_numbers[:10]]
        print_words(file, filtered_words)


if __name__ == "__main__":
    news_directory = get_news_files_directory('json')
    files = [os.path.join(news_directory, f) for f in get_file_list(news_directory)]
    process_files(files)
