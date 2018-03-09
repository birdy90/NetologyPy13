import chardet
import requests
import os


def detect_charset(file_path):
    file = open(file_path, 'rb')
    data = file.read()
    return chardet.detect(data)['encoding']


def read_file(file_path):
    charset = detect_charset(file_path)
    with open(file_path, 'r', encoding=charset) as file:
        data = file.readlines()
    return data


def translate_file(input_file, output_file, source_language, output_language='ru'):
    text = read_file(input_file)
    result = translate_it(text, "{}-{}".format(source_language, output_language))

    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    with open(output_file, 'w+', encoding='utf-8') as file:
        file.write(result)


def translate_it(text, translate_direction):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    params = {
        'key': key,
        'lang': translate_direction,
        'text': text,
    }
    response = requests.get(url, params=params).json()
    print(translate_direction)
    return ' '.join(response.get('text', []))


if __name__ == "__main__":
    basedir = os.path.dirname(__file__)
    files = os.listdir(os.path.join(basedir, 'texts'))

    for source_file in files:
        input_filename = os.path.join(basedir, 'texts', source_file)
        output_filename = os.path.join(basedir, 'translations', source_file)
        lang = os.path.basename(source_file.split('.')[0].lower())
        translate_file(input_filename, output_filename, lang)
