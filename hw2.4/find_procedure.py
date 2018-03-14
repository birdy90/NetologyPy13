# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os
import chardet


def file_extension(filename):
    return filename.split('.')[-1]


def find_in_file(string, filename):
    file_path = os.path.join(migrations_dir, filename)
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            encoding = chardet.detect(data)['encoding']
            lines = data.decode(encoding).split(os.linesep)
            for line in lines:
                if string in line.lower():
                    return True
    except FileExistsError:
        print('Файл не найден ({})'.format(file_path))
    return False


if __name__ == '__main__':

    source_dir = 'Migrations'
    current_dir = os.path.dirname(os.path.abspath(__file__))
    migrations_dir = os.path.join(current_dir, source_dir)
    files = [f for f in os.listdir(migrations_dir) if file_extension(f) == 'sql']

    while len(files) > 1:
        search_string = input('Введите строку: ').lower()
        files = [file for file in files if find_in_file(search_string, file)]
        files_count = len(files)
        if files_count > 10:
            print('... большой список файлов ...')
        else:
            for file in files:
                print('{}/{}'.format(source_dir, file))
        print('Всего {}'.format(files_count))
