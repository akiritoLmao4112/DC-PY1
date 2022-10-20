money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
cap = money_capital
sp=spend
while sp < cap:
    cap-=sp
    month+=1
    sp*=(1+increase)
    cap+=salary


print(month)
