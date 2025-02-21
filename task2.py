# Напиши функцию aggregate,
# которая принимает список чисел и функцию operation,
# выполняющую определённую операцию над парой чисел,
# а также начальное значение.
# Функция должна применить operation ко всем
# элементам списка и вернуть результат.

# Пример:
# [1, 2, 3, 4, 5]
# Передаваемая функция: функция сложения
# результат : 15

# [1, 2, 3, 4, 5]
# Передаваемая функция: функция умножения
# результат : 120


def aggregate(numbers, start_val, operation):
    result = start_val
    for numbers in numbers:
        result = operation(result, numbers)
    return result


def multiplication(x,y):
    return x*y

def summ(x,y):
    return x+y


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(aggregate(numbers, 0, summ))
    print(aggregate(numbers, 1, multiplication))


