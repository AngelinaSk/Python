a = str("Harry")
b = str("Potter")
c = int(10)
d = int(8)
e = int(5)
g = int(1)
k = float(1.5)
l = float(4.5)
m = float(5.2)

#4  Реализовать 15 варианта сравнения int переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль.
if c > d :
    print("c > d")
else:
    print("Not right")

if c <= d:
    print("c <= d")
else:
    print("Not Right")

if c == e:
    print("c == e")
else:
    print("Not right")

if e >= g:
    print("e >= g")
else:
    print("Not right")

if e != d:
    print("e != d")
else:
    print("Not right")

if g <= c:
    print("g <= c")
else:
    print("Not right")

if g < d:
    print("g < d")
else:
    print("Not right")

if d == g:
    print("d == g")
else:
    print("Not right")

if e > g:
    print(" e > g")
else:
    print("Not right")

if c != g:
    print("c != g")
else:
    print("Not right")

if e <= c:
    print("e <= c")
else:
    print("Not right")

if g > c:
    print("g > c")
else:
    print("Not right")

if g == c:
    print("g == c")
else:
    print("Not right")

if d != c:
    print("d != c")
else:
    print("Not right")

if d <= c:
    print("d <= c")
else:
    print("Not right")
#5 Реализовать 9 варианта сравнения Float переменных с операторами >, <, >=, <=, !=. Pезультаты весвести в консоль

if k > l:
    print("k > l")
else:
    print("Not right")

if k < m:
    print("k < m")
else:
    print("Not right")

if k != m:
    print("k != m")
else:
    print("Not Right")

if l >= m:
    print("l >= m")
else:
    print("Not right")

if l != m:
    print("l != m")
else:
    print("Not right")

if l < k:
    print("l < k")
else:
    print("Not right")

if m == l:
    print("m == l")
else:
    print("Not right")
if m <= k:
    print("m <= k")
else:
    print("Not right")
if m < l:
    print("m < l")
else:
    print("Not right")

#6 Реализовать 10 варианта сравнения int переменных с операторами >, <, >=, <=, != и условными выражениями (end, or, not). Pезультаты весвести в консоль.
if (c > d) and (c < e):
    print("Good")
else:
    print("Not right")

if c < g or c > d:
    print("Good")
else:
    print("Not right")

if not c < d:
    print("Good")
else:
    print("Not right")

if not (g < c):
    print("Good")
else:
    print("Not right")

if (g > c) and (c > d):
    print("Good")
else:
    print("Not right")

if (c == d) or (c >= d):
    print("Good")
else:
    print("Not right")
if not (c <= g):
    print("Good")
else:
    print("Not right")

if ( e != g) or (d == e):
    print("Good")
else:
    print("Not right")
if (d >= e) and (g < c):
    print("Good")
else:
    print("Not right")

if not (e != g):
    print("Good")
else:
    print("Not right")

#7  Сделать скрипт используя функцию input(). Функция должна на вход принимать целое число. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"

"""
num = int(input())
if num > 30:
    print("Вы ввели число =", num, "которое > 30")
elif num < 30:
    print("Вы ввели число =", num, "которое < 30")
else:
    print("Вы ввели число =", num, "которое равно 30")
    """

#8Сделать скрипт используя функцию input().1. Функция должна на вход принимать целое число.Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100)) 3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"
"""
nums = int(input())
import random
if nums > random.randint(1,100):
    print("Вы ввели число =", nums, "которое больше сгенерированному числу")
elif nums < random.randint(1,100):
    print("Вы ввели число =", nums, "которое меньше сгенерированному числу")
else:
    print("Вы ввели число =", nums, "которое равно сгенерированному числу")    
"""
#9 Сделать скрипт используя функцию input(). 1. Функция должна на вход принимать целое число.2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))3.Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"
numb = int(input())
import random

if numb > random.randint(1,100):
    if  numb > random.randint(101,200):
       print("Вы ввели число =", numb, "которое, больше сгенерированных чисел")
    else:
        print("Вы ввели число =", numb, "которое, больше и меньше сгенерированных чисел")
elif numb < random.randint(1,100):
    if numb < random.randint(101,200):
       print("Вы вели число =", numb, "которое меньше сгенерированных чисел")
    else:
        print("Вы вели число =", numb, "которое меньше и больше сгенерированных чисел")

