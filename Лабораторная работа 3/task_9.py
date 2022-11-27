salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен
money_capital = 0  # количество денег, чтобы прожить 10 месяцев
delta = 0 # разница расходов и доходов

for i in range(months): # запускаем конечное количество циклов
    delta = spend - salary # формула переменной
    spend *= 1 + increase # увеличение расходов
    money_capital += delta # просчет необходимой фин. подушки

print(round(money_capital)) # финал
