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


def punctuation_del_and_lower(stroka):
    for bukva in stroka:
        if bukva in string.punctuation:
            stroka = stroka.replace(bukva, ' ')
    return stroka.lower()


def word_to_list(stroka):
    spisok_slov = stroka.split()
    return spisok_slov


def glasn_char_count(stroka):
    count_char = []
    for bukva_glasn in glassn_char:
        count_char.append([bukva_glasn, stroka.count(bukva_glasn)])
    return count_char


def word_repeat_count(spisok_slov):
    spword_count = []
    for word in set(spisok_slov):
        spword_count.append([word, spisok_slov.count(word)])
    return spword_count


def main_prog(stroka):
    stroka = punctuation_del_and_lower(stroka)
    spisok_slov = word_to_list(stroka)

    print(f'Слов в этой строке (включая союзы и предлоги): {len(spisok_slov)}')

    print(f'Самое длинное слово: {max(spisok_slov, key=len)}')

    print('Гласных букв в строке:')
    for bukva, povtor in glasn_char_count(stroka):
        print(f'{bukva} : {povtor}')

    print('Сколько раз каждое слово встречается в строке (включая союзы и предлоги):')
    for word, povtor in word_repeat_count(spisok_slov):
        print(f'{word} : {povtor}')


if __name__ == '__main__':
    stroka = input('Введите строку для анализа: ')
    # ниже строка для примера, что бы не вводить с клавиатуры раскоменть её)
    # stroka = 'Мама мыла раму, а девочка Оля сидела за столом и ела кашу! Каша была Очень вкусная, девочка Оля рада!'
    main_prog(stroka)
