"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from datetime import date
import settings

logging.basicConfig(filename='bot.log', level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")  # конфигурация логирования, настройка указания времени

PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {
        'username': settings.PROXY_USERNAME,
        'password': settings.PROXY_PASSWORD
    }}


def greet_user(upedate, context):  # upedate - аргумент - с информацией, пришедшей с платформы Telegramm, context - ?
    print('Вызван /start')
    # print(upedate)
    upedate.message.reply_text('Привет, друг!')


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def planet_func(update, contxt):
    text = update.message.text

    planet = text.split()[1].capitalize()

    pre_answer = ephem.__dict__[planet](date.today())
    answer = ephem.constellation(pre_answer)
    print(answer)
    txt_ans = f"На данный момент {planet.capitalize()} в констеляции: {', '.join(answer)}"
    update.message.reply_text(txt_ans)


def main():
    mybot = Updater(
        settings.API_KEY)  # , use_context=True, request_kwargs=PROXY) # Создаем бота и передаем ему ключ для авторизации на серверах Telegram

    dp = mybot.dispatcher  # сокращаем запись
    dp.add_handler(CommandHandler('start',
                                  greet_user))  # добавляем в перечень существующих команд команду start, вызывающую функция greet_user
    dp.add_handler(CommandHandler('planet', planet_func))  # добавляем обработчика планет
    logging.info('Бот стартовал')
    dp.add_handler(MessageHandler(Filters.text,
                                  talk_to_me))  # добавили в перечень поддерживаемых действий работу с тектом. Вызывает функцию text,talk_to_me

    mybot.start_polling()  # запрашивает обновления с telegmam
    mybot.idle()  # Запускаем бота, он будет работать, пока мы его не остановим принудительно


if __name__ == '__main__':
    main()
