def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    try:
        n = int(input("Введите число: "))
        if n < 2:
            raise ValueError
        break
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите положительное число.")

print("Простые числа до", n, ":", end=" ")
for i in range(2, n + 1):
    if is_prime(i):
        print(i, end=" ")
        print()
print("Непростые числа до", n, ":", end=" ")
for i in range(2, n + 1):
    if not is_prime(i):
        print(i, end=" ")
        print()