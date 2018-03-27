from urllib.parse import urlencode

import requests


class Metrika:

    token = 'AQAAAAACaH7KAATqPU8rJfEPIkyworhlJhhC8Gk'

    def __init__(self):
        request_data = {
            'response_type': 'token',
            'client_id': 'f06cc881a95d49969ee043939939846d'
        }

        url = 'https://oauth.yandex.ru/authorize'
        prepared_url = '?'.join((url, urlencode(request_data)))
        print(prepared_url)

    def get_counter_data(self, counter):
        request_data = {
            'oauth_token': self.token,
            'ids': counter,
            'metrics': 'ym:s:visits,ym:s:pageviews',
            'group': 'Day',
        }
        url = 'https://api-metrika.yandex.ru/stat/v1/data.json' # ?<counter_id>&<metrics>&<dimensions>
        prepared_url = '?'.join((url, urlencode(request_data)))
        print(prepared_url)
        response = requests.get(prepared_url)
        return response.json()


if __name__ == '__main__':
    metrika = Metrika()
    data = metrika.get_counter_data('34311385')
    print(data['query'])
    print(data['data'])