"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.

"""


def discounted(price, discount, max_discount=20):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except ValueError:
        print('Передан некорректрный тип данных')
    try:
        price = abs(price)
        discount = abs(discount)
        max_discount = abs(max_discount)
    except TypeError:
        print('Переданные данные не поддерживаются функцией abs()')
    try:
        if max_discount >= 100:
            raise ValueError('Слишком большая максимальная скидка')
        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)
    except ValueError:
        print('Передан некорректрный тип данных')
    except TypeError:
        print('Переданные данные не поддерживаются')


if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5) if discounted("five", 5) else 'Были переданы некорректыне данные, функция ничего не посчитала')
    print(discounted("сто", "десять")  if discounted("сто", "десять") else 'Были переданы некорректыне данные, функция ничего не посчитала')
    print(discounted(100.0, 5, "10"))
