"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    age = int(input('Введите возраст: '))
    def life_position(age):
        '''
        Функция, определяющая по возрасту, чем должен заниматься пользователь
        в соответствием с условием задачи
        '''
        if age < 7:
            return f"Возраст детского сада"
        elif 7 <= age <= 18:
            return f"Школьный возраст"
        elif 19 <= age <= 24:
            return f"Возраст ВУЗа"
        else:
            return f"Возраст для трудовой деятельности"

    question = life_position(age)
    print(question)




if __name__ == "__main__":
    main()
