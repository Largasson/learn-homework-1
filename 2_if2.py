"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def str_fun(string1, string2):
        if not (isinstance(string1, str) and isinstance(string2, str)):
            return 0
        elif string1 == string2:
            return 1
        elif len(string1) > len(string2):
            return 2
        elif string2 == 'learn':
            return 3

    print(str_fun('строка', 2))
    print(str_fun('learn', 'learn'))
    print(str_fun('lea', 'le'))
    print(str_fun('lear', 'learn'))

if __name__ == "__main__":
    main()
