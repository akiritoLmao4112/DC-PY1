from random import sample
import string

def get_random_password(n) -> str:  #возвращает строки верхнего и нижнего регистра, цифры
    return ''.join(sample(string.ascii_letters + string.digits, n))

print(get_random_password(8))



