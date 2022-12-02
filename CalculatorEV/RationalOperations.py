
def user_inputs_float():
    while True:
        try:
            num = float(input("Введите число: ").replace(",", "."))
            return num
        except ValueError:
            print("Некорректный формат ввода, попробуй еще раз")


def user_selects_operation():
    global operation
    while True:
        operation = (input(f"Введите действие: +, -, *, /: "))
        if operation == "+" or "-" or "/" or "*":
            return operation
        else:
            print("Некорректный формат ввода, попробуй еще раз")


def calculation(firstnum, secondnum):
    if operation == '+':
        res = firstnum + secondnum
        result = round(res, 3)
        return result
    elif operation == '-':
        res = firstnum - secondnum
        result = round(res, 3)
        return result
    elif operation == '*':
        res = firstnum * secondnum
        result = round(res, 3)
        return result
    elif operation == '/':
        if secondnum == 0:
            print("Ошибка! Деление на ноль")
            return "Error"
        else:
            res = firstnum / secondnum
            result = round(res, 3)
            return result


def main_terminal():
    global file
    x = user_inputs_float()
    while True:
        y = user_inputs_float()
        oper = user_selects_operation()
        res = calculation(x, y)
        file = 'results.txt'
        text = f"{x} {oper} {y} = {res}"
        with open('results.txt', 'a') as data:
            data.write(text + "\n")
        print(f"Результат --> {text}\n(записан в файл)")
        if input("Вы хотите повторить расчеты?\n Введите Y чтобы продолжить\n").lower() == "y":
            if input("Вы хотите использовать результаты прошлого расчета?\n "
                     "Введите Y чтобы использовать").lower() == 'y':
                x = res
                continue
            else:
                break
        else:
            # TODO: Сделать выход из приложения без exit code 0
            break
