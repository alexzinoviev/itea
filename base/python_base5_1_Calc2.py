# символ "_" как результат предыдущей операции
# вести лог файл с операциями
# при нажатии на кнопку L - вопроизводить все что было в лог файле
results = ""
ACCEPTABLE_OPERATIONS = ["+", "-", "/", "*"]

def input_var(variable):
    while True:
        value = input(variable)
        if value == "_":
            if results == "":
                print("No previous results, looks like it's first operation. Please enter value again")
                continue
            else:
                return results
        elif value == "l":
            print(read_from_file())
        else:
            return value


def read_from_file():
    list = []
    f = open('cacl_log.txt', 'rt')
    for line in f:
        list.append(line)
    #return operation,x,y



def choose_operation():
    while True:
        chosen_operation = input_var("Choose operation: ")
        if chosen_operation in ACCEPTABLE_OPERATIONS:
            f.write(str(chosen_operation))
            f.write('\n')
            return chosen_operation
        elif chosen_operation == "q":
            exit()
        else:
            print("Incorrect symbol, please retry")
        continue


def calculations(x,y, operation):
    if operation == "+":
        return x+y
    elif operation == "-":
        return x-y
    elif operation == "/":
        return x/y
    elif operation == "*":
        return x*y
    else:
        print("Incorrect symbol, please retry")


while True:
    f = open('cacl_log.txt', 'a')
    try:
        operation = choose_operation()
        x = float(input_var("x?"))
        f.write(str(x))
        f.write('\n')
        y = float(input_var("y?"))
        f.write(str(y))
        f.write('\n')
    except ValueError:
        print("Incorrect value, please retry")
        continue
    results = calculations(x,y, operation)
    f.write(str(results))
    f.write('\n')
    print(results)