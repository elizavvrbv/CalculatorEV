def repeat_or_no():
    # Функция запрашивает у пользователя хочет ли он продолжать работать с комплексными числами
    user_choice = ""
    while user_choice != "Y" or user_choice != "N":
        user_choice = input(
            "Вы хотите продолжить работать с комплексными числами?"
            "Введите Y, если да"
            "Введите N, если нет"
        )
        if user_choice == "N":
            return False
        elif user_choice == "Y":
            return True
        else:
            print("Неправильный ответ, повторите попытку ввода еще раз")


def insert_numbers():
    # Функция запрашивает у пользователя данные
    print('Type of complex number: a + bi\n')
    user_komplex1 = input('Введите первое комплексное число: ')
    user_komplex2 = input('Введите второе комплексное число: ')
    operation = input('Какую операцию хотите ввести? (+, -, *, /)')
    while operation != "+" or operation != "-" or operation != "*" or operation != "/":
        print("Некорректный ввод! Повторите ввод операции")
        operation = input('Какую операцию хотите ввести? (+, -, *, /)')
    with open('results.txt', 'a') as data:
        data.write(f'({user_komplex1}){operation}({user_komplex2}) = ')
    return [user_komplex1, user_komplex2, operation]


def take_rational_part(user_number):
    # Функция возвращает действительную часть числа
    rational_part = []
    for k in range(0, len(user_number)):
        if user_number[k] != ' ':
            rational_part.append(user_number[k])
        else:
            break
    rational_part = float(''.join(rational_part))
    return rational_part


def take_imaginary_part(user_number):
    # Функция возвращает мнимую часть числа
    imaginary_part = []
    for i in range(0, len(user_number)):
        if user_number[i] == 'i':
            while user_number[i] != ' ':
                imaginary_part.insert(0, user_number[i - 1])
                i -= 1
    imaginary_part.pop(0)
    imaginary_part = float(''.join(imaginary_part))
    return imaginary_part


def take_symbol(user_number):
    # Функция возвращает - или + между действительной и мнимой частью числа
    symbol = []
    for l in range(0, len(user_number)):
        if (user_number[l] == '-' and l != 0) or (user_number[l] == '+' and l != 0):
            symbol.append(user_number[l])
    symbol = ''.join(symbol)
    return symbol


def addition(r1, s1, i1, r2, s2, i2):
    # Функция сложения двух комплексных чисел
    result = [(r1 + r2)]
    if s1 == '+' and s2 == '+':
        result.append(i1 + i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1 - i2)
    elif s1 == '-' and s2 == '+':
        result.append(i2 - i1)
    else:
        result.append(-(i1 + i2))
    return result


def deduction(r1, s1, i1, r2, s2, i2):
    # Функция вычитания второго комплексного числа из первого
    result = [(r1 - r2)]
    if s1 == '+' and s2 == '+':
        result.append(i1 - i2)
    elif s1 == '+' and s2 == '-':
        result.append(i1 + i2)
    elif s1 == '-' and s2 == '+':
        result.append(-i2 - i1)
    else:
        result.append(i2 - i1)
    return result


def multiply(r1, s1, i1, r2, s2, i2):
    # Функция умножения двух комплексных чисел
    result = [(r1 * r2)]
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        result.append(-i1 * i2)
    else:
        result.append(i1 * i2)
    if s1 == "+":
        result.append(r2 * i1)
    else:
        result.append(-r2 * i1)
    if s2 == "+":
        result.append(r1 * i2)
    else:
        result.append(-r1 * i2)
    result[0] = result[0] + result[1]
    result[1] = result[2] + result[3]
    result.pop(3)
    result.pop(2)
    return result


def division(r1, s1, i1, r2, s2, i2):
    # Функция деления двух комплексных чисел
    numerator = [(r1 * r2)]
    denominator = []
    result = []
    if s1 == "+" and s2 == "+" or s1 == "-" and s2 == "-":
        numerator.append(i1 * i2)
    else:
        numerator.append(-i1 * i2)
    if s1 == "-":
        numerator.append(-r2 * i1)
    else:
        numerator.append(r2 * i1)
    if s2 == "+":
        numerator.append(-r1 * i2)
    else:
        numerator.append(r1 * i2)
    numerator[0] = numerator[0] + numerator[1]
    numerator[1] = numerator[2] + numerator[3]
    numerator.pop(3)
    numerator.pop(2)
    denominator.append(r2 ** 2 + i2 ** 2)
    result.append(numerator[0] / denominator[0])
    result.append(numerator[1] / denominator[0])
    return result


def record_in_file(result):
    # Запись результатов в файл
    with open('results.txt', 'a') as data:
        if result[1] != 0:
            for i in range(0, 2):
                if result[i] > 0 and i == 1:
                    data.write('+ ')
                elif result[i] < 0 and i == 1:
                    result[i] = -result[i]
                    result[i] = str(result[i])
                    data.write('- ')
                    data.write(result[i])
                else:
                    result[i] = str(result[i])
                    data.write(result[i])
                if i != 1:
                    data.write(' ')
            data.write('i\n')
        else:
            result[0] = str(result[0])
            data.write(f'{result[0]}\n')


def main_terminal():
    repeat = True
    while repeat:
        operands = insert_numbers()
        if operands[2] == "+":
            record_in_file(addition(take_rational_part(operands[0]),
                                    take_symbol(operands[0]),
                                    take_imaginary_part(operands[0]),
                                    take_rational_part(operands[1]),
                                    take_symbol(operands[1]),
                                    take_imaginary_part(operands[1])))
        elif operands[2] == "-":
            record_in_file(deduction(take_rational_part(operands[0]),
                                     take_symbol(operands[0]),
                                     take_imaginary_part(operands[0]),
                                     take_rational_part(operands[1]),
                                     take_symbol(operands[1]),
                                     take_imaginary_part(operands[1])))
        elif operands[2] == "*":
            record_in_file(multiply(take_rational_part(operands[0]),
                                    take_symbol(operands[0]),
                                    take_imaginary_part(operands[0]),
                                    take_rational_part(operands[1]),
                                    take_symbol(operands[1]),
                                    take_imaginary_part(operands[1])))
        else:
            record_in_file(division(take_rational_part(operands[0]),
                                    take_symbol(operands[0]),
                                    take_imaginary_part(operands[0]),
                                    take_rational_part(operands[1]),
                                    take_symbol(operands[1]),
                                    take_imaginary_part(operands[1])))
        repeat = repeat_or_no()
