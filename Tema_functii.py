my_function = [1, 5, -3, 'abc', [12, 56, 'cad']]
#returnare 3
def my_fct (param_1, param_2, param_3):
    print(param_1+param_2+param_3)
my_fct(1, 5, -3)
#sau
def sum(x,y,z):
    return x+y+z
print(sum(1, 5, -3))

#returnare 0
for i in my_function:
    if i != 0:
        print (0)

#returnare 6 - nu stiu daca trebuia scris altfel ultimul parametru din lista
my_other_function = [ 2, 4, "abc", "param_1" == 2]
def my_fct1 (var1, var2):
    print(var1+var2)
my_fct1(2,4)

#recursivitate

#suma tuturor elementelor de la 0 la n

def sum_fct1(n):
    if n ==0:
        return n
    return n+ sum_fct1(n-1)
print(sum_fct1(13))

#suma nr pare si impare de la 0 la n

list = [0,1,2,3,4,5,6,7,8,9,10]
suma_par = 0
suma_impar = 0
for i in list:
    if i%2!=0:
        suma_impar = suma_impar + i
    else:
        suma_par = suma_par + i
print(suma_par)
print(suma_impar)

#sau
#1 - aici teoretic trebuia sa-mi dea 30, nu 20. Presupun ca ia in calcul doar numerele pana la 10, nu inclusiv
sum = 0
for i in range (10):
    if i % 2==0:
        sum= sum +i
print(sum)
#2
sum = 0
for i in range (10):
    if i % 2 != 0:
        sum= sum +i
print(sum)

#sau
#1
def sum_of_even(n):
    if n==0:
        return 0
    if not n % 2 == 0:
        return sum_of_even(n-1)
    else:
        return n + sum_of_even(n-1)

print(sum_of_even(10))
#2
def sum_impare(num1,num2):
    if num1>num2:
        return 0

    return num1+sum_impare(num1+2,num2)
num1=1
print("Stabileste limita:")
num2=int(input())
print("Suma numerelor impare este:",sum_impare(num1,num2))

#numar intreg
#1
numarul = input("Enter the input: ")

try:
    int(numarul)
    este = True
except ValueError:
    este = "0"

print(este)

#2 - nu inteleg de ce la acest exemplu imi da 0, chiar daca pun numere intregi
numarul1 = input("Enter the input: ")
if numarul1 == int():
    print (True)
else:
    print("0")
