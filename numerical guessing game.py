                                           #✅👾импортируем модуль random👾✅
from random import *
import time
count = 0


                                                   #✅👾Приветсвие👾✅
def privet():
            print(choice(['🤖Приветствую в числовой угадайке🤖', '👽Добро пожаловать в числовую угадайку!👽', '🤠Рад вас видеть в числовой угадайке🤠']))

                                                  #✅👾набор фраз👾✅

nabor_true = ['Вы угадали!✅', '😺Молодцы! Вы угадали ', 'Поздравляю, вы угадали👩‍🎓', '😀Ого! Угадали', '🤓Я вас поздравлю, вы угадали']
nabor_false = ['🤦‍♂️Вы не угадали', 'Очень жаль, не угадали', '👨‍🏫К сожалению вы не угадали', 'Что-ж не угадали..', 'Попробуйте еще раз, вы не угадали.']
nabor_bol_false = ['😬Число больше загаданного, не угадали..', '👀‍Далеко ушли, но не угадали', '👺Выше горы, не угадали', 'Далековато..']
nabor_men_false = ['💩Число меньше загаданного, не угадали...', '🤕Летите низко..', '👎Не угадали, слишком мало!', '💀Я думаю что это мало..']


                                              #✅👾основной цикл с ответом.👾✅
def chicl():
    count = 0
    privet()

    while True:
        g = randint(1, 101)
        ch = input('🧛‍♀️Введите число от 1 до 100, а я его загадаю:\n')
        print('Загадываю число...🤔')
        time.sleep(2)
        if not is_nub(ch):
            print('По моим данным, вы ввели неправильно🕵️‍♂️')
            print('А может быть все-таки введем целое число от 1 до 100?😡')
            continue
        ch = int(ch)

        if ch == g:
            print(choice(nabor_true))
            print('Загаданное число было:', g)
        elif ch > g:
            print(choice(nabor_men_false))
            print('загаданное число было:', g)
        elif ch < g:
            print(choice(nabor_bol_false))
            print('загаданное число было:', g)
        count += 1
        print('попытка #', count)
        return povtor()
        break


                                              #✅👾защита от дурака👾✅


def is_nub(i):
    if i.isdigit() and 1 <= int(i) <= 100:
        return True
    else:
        return False





                                               #✅👾повтор если уже ссыграл👾✅
def povtor():
    povtor = input('Хотите ссыграть еще раз? [да/нет]:\n')
    if povtor == 'да':
        print('🕙Перезапускаю числовую угадайку...🕚')
        time.sleep(3)
        chicl()
    elif povtor == 'нет':
        print('Тогда до встречи')






chicl()

print('*'*100, ' 😎Спасибо, что играли в числовую угадайку. Еще увидимся...', '*'*100, sep='\n')