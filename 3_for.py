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
    res_of_length = []
    for product_dict in lst:
        temp = sum(product_dict['items_sold'])
        length_of_seq =  len(product_dict['items_sold'])
        print(f"Суммарное количество продаж смартфона {product_dict['product']}: {temp}")
        print(f"Среднее количество продаж смартфона {product_dict['product']}: {round(temp / length_of_seq)}")
        res.append(temp)
        res_of_length.append(length_of_seq)

    medieval_length = sum(res_of_length) / len(lst)
    print(f'Суммарное количество продаж всех смартфонов: {sum(res)}')
    print(f'Ссреднее количество продаж всех смартфонов: {round(sum(res) / medieval_length)}')


if __name__ == "__main__":
    main()
