from string import ascii_letters
class PlanetNameError(Exception):
    pass


planets = {'Марс': 'Mars', 'Меркурий': 'Mercury', 'Венера': 'Venus',
           'Юпитер': 'Jupiter', 'Сатурн': 'Saturn',
           'Уран': 'Uranus', 'Нептун': 'Neptune'}


def valid_planet_name(text):
    '''
     проверка на корректность планеты, перевод с русского на английский
    '''

    input_lst = text.split()
    if len(input_lst) != 2:
        return PlanetNameError(
            'Как-то некорректно сформулирован запрос. То ли планеты такой нет, то ли с синтаксисом кто-то напутал... Попробуй еще раз, шаблон слудующий: /planet планета')
    input_planet = input_lst[-1].capitalize()
    en_planet = all(map(lambda c: c in ascii_letters, input_planet))
    if en_planet and input_planet in planets.values():
        return input_planet
    elif not en_planet and input_planet in planets.keys():
        return planets.get(input_planet)
    else:
        return PlanetNameError(
            'Как-то некорректно сформулирован запрос. То ли планеты такой нет, то ли с синтаксисом кто-то напутал... Попробуй еще раз, шаблон слудующий: /planet планета')

if __name__ == '__main__':
    try:
        text = '/planet маравс'
        print(valid_planet_name(text))
    except PlanetNameError as err:
        print(err)
