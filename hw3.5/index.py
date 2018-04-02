import chardet
import math
import osa
import os

current_directory = os.path.dirname(os.path.abspath(__file__))


def read_file(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        encoding = chardet.detect(data)['encoding']
        return data.decode(encoding).split('\n')


def temperature_converter():
    data = read_file(os.path.join(current_directory, 'files', 'temps.txt'))

    # webservicex не работает
    client = osa.Client('http://www.w3schools.com/xml/tempconvert.asmx?WSDL')

    overall_count = len(data)
    processed_data = [client.service.FahrenheitToCelsius(Celsius = fahrenheit.split(' ')[0]) for fahrenheit in data]
    average = sum([int(d) for d in processed_data]) / overall_count
    print('Средняя температура: {}'.format(average))


def currency_converter():
    data = read_file(os.path.join(current_directory, 'files', 'currencies.txt'))
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')

    prepared_data = [{
        'licenseKey': '',
        'fromCurrency': cur.split(' ')[2],
        'toCurrency': 'RUB',
        'amount': int(cur.split(' ')[1]),
        'rounding': True
    } for cur in data]

    processed_data = [math.ceil(client.service.ConvertToNum(**cur)) for cur in prepared_data]
    result = sum([d for d in processed_data])
    print('Затраты на поездку в рублях: {}'.format(result))


def distance_converter():
    data = read_file(os.path.join(current_directory, 'files', 'travel.txt'))

    # ссылка, которую я получаю в гугле по запросу "miles to meters wsdl"
    client = osa.Client('http://www.webservicex.net/WS/WSDetails.aspx?WSDL')

    prepared_data = [item for item in data]

    processed_data = [round(client.service.ConvertToNum(**length), 2) for length in prepared_data]
    result = sum([d for d in processed_data])
    print('Суммарная длина пути: {}'.format(result))


if __name__ == '__main__':
    # temperature_converter()  # xml.etree.ElementTree.ParseError: mismatched tag: line 68, column 16 при запросе
    currency_converter()
    # distance_converter()  # webservicex не работает
