money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
cap = money_capital
count = 0 #счетчик месяцев
while cap > spend - salary:
    if count > 0:  #считаем со второго месяца
        spend += spend * increase
    cap = cap + salary - spend
    count += 1
print("Количество месяцев, которое можно протянуть без долгов:", count)
