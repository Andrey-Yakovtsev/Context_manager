
from datetime import datetime
from pprint import pprint
import time


def starter():
    start = time.time()
    dict_collector('reciepts_initial.txt')
    finish = time.time()
    runtime = finish - start
    print(runtime)

def dict_collector(file_path):
    with open(file_path, 'r') as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            time.sleep(1)
            counter = file_work.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) # - временный словарь с ингридиетом
                ingridient = file_work.readline().strip().split(' | ') # - вот так перемещаемся по файлу
                # for item in ingridient:
                dish_items['ingredient_name'] = ingridient[0]
                dish_items['quantity'] = ingridient[1]
                dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file_work.readline()

    return(menu)




def get_shop_list_by_dishes(dishes, persons:int):
    menu = dict_collector('reciepts_initial.txt')
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item
                else:
                    shopping_list.update(items_list)

        # print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")

if __name__ == '__main__':
    get_shop_list_by_dishes(['Омлет', 'Фахитос'], 10)
