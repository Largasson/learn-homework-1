"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    lst = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]}]
    res = []
    for i in range(len(lst)):
        res.append(sum(lst[i]['items_sold']))

    print(f'Суммарное количество продаж смартфона iPhone 12: {res[0]}')
    print(f'Среднее количество продаж смартфона iPhone 12: {round(res[0] / 12)}')
    print(f'Суммарное количество продаж смартфона Xiaomi Mi11: {res[1]}')
    print(f'Среднее количество продаж смартфона Xiaomi Mi11: {round(res[1] / 12)}')
    print(f'Суммарное количество продаж смартфона Samsung Galaxy 21: {res[2]}')
    print(f'Среднее количество продаж смартфона Samsung Galaxy 21: {round(res[2] / 12)}')
    print(f'Суммарное количество продаж всех смартфонов: {sum(res)}')
    print(f'Ссреднее количество продаж всех смартфонов: {round(sum(res) / 12)}')


if __name__ == "__main__":
    main()
