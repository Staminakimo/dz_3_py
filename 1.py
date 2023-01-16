# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


my_list = []
k = int(input())
for i in range(1, k+1):
    my_list.append(fib(i))
print(my_list)

my_list_str = str(my_list)

fibonachi = open('fib.txt', mode='w+', encoding='utf-8')
print(fibonachi)
fibonachi.write(my_list_str)
fibonachi.close()
