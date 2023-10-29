# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.

# объявление функции
def get_next_prime(num):
    for nums in range(num + 1, 10000):
        c = 0
        for i in range(1, nums + 1):
            if nums % i == 0: 
                c = c + 1       
        if c < 3:
            return nums
            break

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))