from pprint import pprint
def ss(n): #создадим функцию для вывода списка словарей.
    return [{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)} for i in range(n+1)] #успользуя list comprehension запишем словари в список

pprint(ss(15))