# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
# числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
# num_translate_adv("One")
# "Один"
# num_translate_adv("two")
# "два"


def num_translate(sttr):
    dict_num = {'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}
    if sttr.lower() in dict_num:
        if sttr[0].isupper():
            return dict_num[sttr.lower()].capitalize()
        else: return dict_num[sttr]
    else: return None

print(num_translate(input('Введите число на английском языке: ')))