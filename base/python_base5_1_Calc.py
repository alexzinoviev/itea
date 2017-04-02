# калькулятор
# операция + - / *
# ожидаем числа
# q - выйти


global operation

def input_var(variable):
    return input(variable)

def operaton(x,y,operation):
    return x + operation + y

# def add(x,y):
#     return x+y
#
# def minus(x,y):
#     return x - y
#
# def devide(x,y):
#     return x / y
#
# def multiplication(x,y):
#     return x * y

def choose_operation():
     #global operation
     operation = input_var("Choose operation: ")
     operaton(x,y,operation)

     #
     # if operation == "+":
     #     add(x,y)
     # elif operation == "-":
     #     minus(x,y)
     # elif operation == "/":
     #     devide(x,y)
     # elif operation == "*":
     #     multiplication(x,y)
     # else:
     #     print("Incorrect symbol, please retry")

def print_results():
    if operation == "+":
        print(add(x,y))
    elif operation == "-":
        print(minus(x,y))
    elif operation == "/":
        print(devide(x,y))
    elif operation == "*":
        print(multiplication(x,y))

while True: #input_var("Quit?") != "q":
    try:
        x = int(input_var("x?"))
        y = int(input_var("y?"))
    except ValueError:
        print("Incorrect value, please retry")
        continue
    choose_operation()
    print_results()
    if input_var("Quit?") == "q":
        break
    continue