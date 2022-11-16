from random import sample
import string    # данную библиотеку мы будем использовать для возвращения строк

def get_random_password(n) -> str:  # возвращает строки верхнего и нижнего регистра, цифры
    return ''.join(sample(string.ascii_letters + string.digits, n))

print(get_random_password(8))



