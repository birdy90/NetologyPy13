import vk
import getpass


def check_errors(response):
    if response['error']:
        code = response['error']['error_code']
        if code == 5:
            print('Авторизация не удалась')
        elif code == 6:
            print('Слишком много запросов в секунду')
        elif code in (27, 28):
            print('Ключ доступа приложения недействителен')
        else:
            print('Ошибка запроса. Код {}'.format(code))


if __name__ == "__main__":
    friendIds = [17688555, 1684276]

    login = input('Логин: ')

    # getpass.getpass() почему-то не принимает ввод, после ввода логина я попадаю в какое-то
    # непонятное ожидание
    password = input('Пароль: ')

    session = vk.AuthSession('6408348', login, password, scope='friends')
    vk_api = vk.API(session)
    data = vk_api.friends.getMutual(target_uids=friendIds, v=5.73)

    print('Общие друзья:')
    for friend in data:
        friend_data = vk_api.users.get(user_ids=friend['id'], v=5.73)
        print('с пользователем {} {}:'.format(friend_data[0]['first_name'], friend_data[0]['last_name']))

        common_friends = vk_api.users.get(user_ids=friend['common_friends'], v=5.73)

        for person in common_friends:
            print('\t{} {}'.format(person['first_name'], person['last_name']))
        print()
