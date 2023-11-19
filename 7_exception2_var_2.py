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
    price = float(price)
    discount = float(discount)
    max_discount = int(max_discount)
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError
    if discount >= max_discount:
        return price
    else:
        return price - (price * discount / 100)

if __name__ == "__main__":
    values = ((100, 2), (100, "3"), ("100", "4.5"), ("five", 5), ("сто", "десять"), (100.0, 5, "10"), (100.0,))
    for value in values:
        if len(value) == 2:
            try:
                print(discounted(value[0], value[1]))
            except ValueError:
                print('Переданные данные некорректны')
            except TypeError:
                print('Переданные данные некорректны')
        elif len(value) == 3:
            try:
                print(discounted(value[0], value[1]), value[2])
            except ValueError:
                print('Переданные данные некорректны')
            except TypeError:
                print('Переданные данные некорректны')
        else:
            print('Непонятки с входными данными, перепроверь')
