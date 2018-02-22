def read_data():
    import os
    base_dir = os.path.dirname(__file__)
    lines = open(os.path.join(base_dir, 'data.txt'), 'r', encoding='utf-8').readlines()
    lines = [l[:-1].lower() for l in lines]  # убираем переносы строк и приводим к единому виду
    cook_book = {}
    i = 0
    while i < len(lines):
        cook_book[lines[i]] = []
        number_of_ingredients = int(lines[i+1])
        for j in range(0, number_of_ingredients):
            data = lines[i + j + 2].split(' | ')
            ingredient = {
                'ingredient_name': data[0],
                'quantity': int(data[1]),
                'measure': data[2],
            }
            cook_book[lines[i]].append(ingredient)
        i += number_of_ingredients + 3
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in read_data()[dish]:
            new_shop_list_item = dict(ingredient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
