# Модуль random
import random

# Випадкові слова та імена
name = ('Владислав', 'Коля', 'Олексій', 'Максим')
verb = ('любить', 'обожнює', 'недолюблює', 'хоче')
verb2 = ('програмувати', 'творити', 'навчатися програмуванню', 'грати в ігри', 'спати')

# Генератор випадкових речень
random_list = [name, verb, verb2]


def random_phrase():
    result_string = ""
    for i in range(0, 3):
        random_index = random.randrange(0, 4)
        result_string = result_string + \
            random_list[i][random_index] + " "

    return result_string
    
print(random_phrase())