ticket=int(input('Введите количество посетителей'))
price = 0
for i in range (ticket):
    i += 1
    while True:
        age_visitors=int(input(f'Введите возраст посетителя №{i}'))
        if age_visitors < 18:
            price += 0
            print('Цена: 0')
            break
        elif 18 <= age_visitors < 25:
            price += 990
            print('Цена: 990')
            break
        else:
            price += 1390
            print('Цена: 1390')
            break
if ticket > 3:
    full_price = 0.9
else:
    full_price = 1
print('Сумма к оплате  руб.', price * full_price)