msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

msg_3 = "Yeah... division by zero. Smart move..."

msg_4 = "Do you want to store the result? (y / n):"

msg_5 = "Do you want to continue calculations? (y / n):"

opers = ['+', '-', '*', '/']

memory = 0

continue_calculation = True

while continue_calculation:

    result = 0
    read_calc = str(input(msg_0))
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
        if y != '0':
            print(msg_3)
            continue
        result = x / y
        print(result)

    answer = ''
    while answer != 'y' and answer != 'n':
        answer = str(input(msg_4))
        if answer == 'y':
            memory = result

    new_calc = ''
    while new_calc != 'y' and new_calc != 'n':
        new_calc = str(input(msg_5))
        if new_calc == 'n':
            continue_calculation = False

