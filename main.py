"""
Задание:
Напишите программу, которая анализирует текст, введенный пользователем, и выполняет следующие действия:
Подсчитывает количество слов в тексте.
Определяет самое длинное слово в тексте.
Подсчитывает количество гласных букв (а, е, ё, и, о, у, ы, э, ю, я) в тексте.
Выводит количество раз, которое каждое слово встречается в тексте.
Требования к программе:
Используйте цикл for для итерации по словам в тексте.
Программа должна игнорировать регистр букв (т.е. "А" и "а" считаются одинаковыми).
Учтите возможность наличия знаков препинания в тексте (они не должны учитываться как часть слов).
"""
import string

glassn_char = 'аеёиоуыэюя'


def punctuation_del_and_lower(stroka1):
    for _ in stroka1:
        if _ in string.punctuation:
            stroka1 = stroka1.replace(_, ' ')
    return stroka1.lower()


def word_count(stroka1):
    spisokslov = stroka1.split()
    return spisokslov


def glasn_char_count(stroka1):
    count_char = []
    for _ in glassn_char:
        count_char.append([_, stroka1.count(_)])
    return count_char


def word_repeat_count(spisokslov):
    spword_count = []
    for _ in set(spisokslov):
        spword_count.append([_, spisokslov.count(_)])
    return spword_count


def main_prog(stroka1):
    stroka1 = punctuation_del_and_lower(stroka1)
    spisokslov = word_count(stroka1)
    print(f'Слов в этой строке (включая союзы и предлоги): {len(spisokslov)}')
    print(f'Самое длинное слово: {max(spisokslov, key=len)}')
    print('Гласных букв в строке:')
    for _ in glasn_char_count(stroka1):
        print(f'{_[0]} : {_[1]}')
    print('Сколько раз каждое слово встречается в строке (включая союзы и предлоги):')
    for _ in word_repeat_count(spisokslov):
        print(f'{_[0]} : {_[1]}')


if __name__ == '__main__':
    stroka1 = input('Введите строку для анализа: ')
    # ниже строка для примера, что бы не вводить с клавиатуры раскоменть её)
    # stroka1 = 'Мама мыла раму, а девочка Оля сидела за столом и ела кашу! Каша была Очень вкусная, девочка Оля рада!'
    main_prog(stroka1)
