msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

msg_6 = " ... lazy"

msg_7 = " ... very lazy"

msg_8 = " ... very, very lazy"

msg_9 = "You are"

msg_10 = "Are you sure? It is only one digit! (y / n)"

msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"

msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

opers = ['+', '-', '*', '/']

memory = 0

continue_calculation = True


def is_one_digit(v):
    # if v == 5.0:
    #     return False
    return -10 < v < 10 and v.is_integer()


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_6
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_7
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


while continue_calculation:

    result = 0
    read_calc = str(input(msg_0+"\n"))
    read_calc_arr = read_calc.split(' ')
    x = read_calc_arr[0]
    oper = read_calc_arr[1]
    y = read_calc_arr[2]

    if x == 'M':
        x = str(memory)

    if y == 'M':
        y = str(memory)

    if not x.replace('.', '').isnumeric() or not y.replace('.', '').isnumeric():
        print(msg_1)
        continue

    elif not opers.__contains__(oper):
        print(msg_2)
        continue

    x = float(x)
    y = float(y)

    check(x, y, oper)

    if oper == '+':
        result = x + y
        print(result)
    if oper == '-':
        result = x - y
        print(result)
    if oper == '*':
        result = x * y
        print(result)
    if oper == '/':
        if y == 0:
            print(msg_3)
            continue
        result = x / y
        print(result)


    answer = ''
    memory_check = True
    while memory_check:
        answer = str(input(msg_4+"\n"))
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    question = str(input(globals()[f"msg_{msg_index}"]+"\n"))
                    if question == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            memory_check = False
                            break
                    if question == 'n':
                        memory_check = False
                        break
            else:
                memory = result
                memory_check = False
        if answer == 'n':
            memory_check = False

    new_calc = ''
    while new_calc != 'y' and new_calc != 'n':
        new_calc = str(input(msg_5+"\n"))
        if new_calc == 'n':
            continue_calculation = False
