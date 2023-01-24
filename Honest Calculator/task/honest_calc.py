msg_0 = "Enter an equation"

msg_1 = "Do you even know what numbers are? Stay focused!"

msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

opers = ['+', '-', '*', '/']

while True:
    read_calc = str(input(msg_0))
    read_calc_arr = read_calc.split(' ')
    x = read_calc_arr[0]
    oper = read_calc_arr[1]
    y = read_calc_arr[2]
    if not x.replace('.', '').isnumeric() or not y.replace('.', '').isnumeric():
        print(msg_1)
        continue

    elif not opers.__contains__(oper):
        print(msg_2)
        continue
    break
