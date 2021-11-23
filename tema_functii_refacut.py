#1

def my_function(*args,**kwargs):
     return(sum(x for x in args if type(x) == int))

print(my_function(1,-3,5,'abc',[12,56,'cad']))
print(my_function())
print(my_function(2,4,'abc',param1=2))

#2
#a
def sum_all(n):
    return n + sum_all(n-1) if n else 0
print(sum_all(10))
#b
def sum_par(n):
    count = 0
    for i in range(0, n, 1):
        if(i % 2 == 0):
            count += i
    return count
print(sum_par(10))
#c
def sum_impar(n):
    count = 0
    for i in range(0, n, 1):
        if(i % 2 != 0):
            count += i
    return count
print(sum_impar(11))

#3
def my_integerfunction(value):
    try:
        value_intreger= int(value)
        print(value)
    except ValueError as e:
        print("0")
my_integerfunction(input('Numarul este:'))