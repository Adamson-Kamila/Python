'''Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S
 журавликов. Сколько журавликов сделал каждый ребенок, если известно,
 что Петя и Сережа сделали одинаковое количество журавликов, а Катя
 сделала в два раза больше журавликов, чем Петя и Сережа вместе?
*Пример:*
6 -> 1  4  1
24 -> 4  16  4
    60 -> 10  40  10'''

s = int(input('Введите количесто журавликов: '))

if s%3 !=0:
    print('Введите число, деление которого по модулю даёт в остатке 0: ')

if s%3 ==0:
    boys = s//3//2
    girl = boys*2*2
    print(f'Мальчики сделали по {int(boys)} журавликов, девочка сделала {int(girl)} журавликов')