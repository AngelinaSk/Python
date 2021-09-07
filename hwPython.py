#1
name = str("Angelina")
print(name)
#2
age = int(24)
print(age)
#3
a = float(4.5)
print(a)
#4
n = bytes(8)
print(n)
#5
new_list = list()
name_1 = "Angelina"
name_2 = "Vadim"
name_3 = "Vladislaw"
new_list =[name_1, name_2, name_3]
for i in new_list:
    print('name =' , i)
#6
k = tuple('hello, world!')
print(k)
#7
s = set('Partly',)
print(s)
#8
box = frozenset('red',)
print(box)
#9
d = dict(short='dict', long='dictionary')
print(d)

#10.1
print('name=', name, type(name))

#10.2
print('age =', age, type(age))

#10.3
print('a = ', a, type(a))
#10.4
print('n=', n, type(n))
#10.5
print(new_list, type(new_list))
#10.6
print(k,type(k))
#10.7
print(s, type(s))
#10.8
print(box, type(box))
#10.9
print(d, type(d))
#11
names=str('Angelina')
lastname = str('Oksak')
summa = (names + lastname)
print(summa)
#12
a1 = int(7)
b2 = int(2)
summa_1= (a1 + b2)
print(summa_1)
#13
division = (a1 / b2)
print(division)
#14
multiplication = (a1 * b2)
print(multiplication)
#15
at = (a1 // b2)
print(at)
#16
at1 =(a1 % b2)
print(at1)
