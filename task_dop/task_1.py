# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# num_translate("one")
# "один"
# num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, 
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

# one two three four five six seven eight nine ten
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
    if sttr in dict_num: return dict_num[sttr]
    else: return None

print(num_translate(input('Введите число на английском языке: ')))
