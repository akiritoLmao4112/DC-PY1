from random import randint

def get_unique_list_numbers() -> list[int]: # TODO написать функцию для получения списка уникальных целых чисел
    min_ = -10
    max_ = 10
    list_ = []
    l = 15
    while len(list_) != l:
        list_ = list(list_)
        list_.append(randint(min_, max_))
        list_ = set(list_)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
