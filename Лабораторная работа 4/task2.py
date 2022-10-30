def get_count_char(str_):                         #TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = str_.lower()
    a_dict = {}
    default_count = 0
    for i in str_:
        if i.isalpha():
            a_dict [i] = a_dict.get(i , default_count) + 1
    return a_dict

def procent(dict):
    m = 0
    for j in dict:
        m += dict[j]
    for j in dict:
        dict[j] = round((dict[j]/m)*100, 2)
    return dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
