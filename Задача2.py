# Задайте натуральное число N. Напишите программу, которая
# составит список простых множителей числа N.
#24
#2 2 2 3

num = int(input("Введите число: "))
i = 2
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(lst)