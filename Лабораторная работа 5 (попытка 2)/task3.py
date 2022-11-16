from random import randint

def get_unique_list_numbers(len_) -> list[int]: # TODO написать функцию для получения списка уникальных целых чисел
    min_ = -10 # нижняя граница интервала случайных чисел
    max_ = 10  # нижняя граница интервала случайных чисел
    list_ = [] # создаем список в котором будут содержаться случайные числа
    while len(list_) != len_:
        list_ = list(list_)
        list_.append(randint(min_, max_)) # методом randint вызовем случайное числа из интервала случайных чисел
        list_ = set(list_) # чтобы избежать повторений мы перезадаем нащ список в множество
    return list_


list_unique_numbers = get_unique_list_numbers(15)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
