# coding=utf-8

import os


def get_news_files_directory():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_directory, 'news')


def get_file_list(dir):
    return os.listdir(dir)


def detect_charset(filepath):
    import chardet
    file = open(filepath, 'rb')
    data = file.read()
    return chardet.detect(data)['encoding']


def read_file(filepath):
    charset = detect_charset(filepath)
    file = open(filepath, 'r', encoding=charset)
    return file.readlines()


def count_long_words(words):
    long_words = [w for w in words if len(w) > 6]
    word_numbers = {word: {'word':word, 'number': long_words.count(word)} for word in long_words}
    word_numbers = word_numbers.values()
    sorted_word_numbers = sorted(word_numbers, key=lambda item: item['number'], reverse=True)
    return sorted_word_numbers


def print_words(filename, words):
    print("Самые популярные слова в файле %s" % filename)
    for word in words:
        print("%s: %s" %(word['word'], word['number']))
    print()


def get_file_contents(filelist):
    words = []
    for file in filelist:
        [words.extend(line[:-1].split(' ')) for line in read_file(file)]
        sorted_word_numbers = count_long_words(words)
        filtered_words = [word for word in sorted_word_numbers[:10]]
        print_words(file, filtered_words)

    return words


def run():
    news_directory = get_news_files_directory()
    files = [os.path.join(news_directory, f) for f in get_file_list(news_directory)]
    words = get_file_contents(files)

run()