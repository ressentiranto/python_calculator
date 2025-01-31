def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
def factorial(a):
    if a == 0:
        return 1
    result = 1
    for i in range(1, int(a)+1):
        result *= i
    return result
def main():
    print("Добро пожаловать в калькулятор на Python!")
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    operation = input("Выберите операцию (+, -, *, /, !): ")

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    elif operation == "!":
        result = factorial(num1)
    else:
        print("Неверная операция!")
        return

    print(f"Результат: {num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    main()