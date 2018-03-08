import os


def ingredient_from_line(line):
    data = line.split(' | ')
    ingredient = {
        'ingredient_name': data[0],
        'quantity': int(data[1]),
        'measure': data[2],
    }
    return ingredient


def read_data():
    base_dir = os.path.dirname(__file__)
    cook_book = {}

    with open(os.path.join(base_dir, 'data.txt'), 'r', encoding='utf-8') as datafile:
        lines = datafile.readlines()
        lines = [l.strip().lower() for l in lines]

        i = 0
        dish = None
        for line in lines:
            if not line:
                dish = None
                continue
            elif dish is None:
                cook_book[dish] = []
                dish = line
                continue

            cook_book[dish].append(ingredient_from_line(line))

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = read_data()
    for dish in dishes:
        for ingredient in cook_book[dish]:
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
