debug = False
def decimal_system():
    global debug
    if debug is True:
        print("This is a test so you know debug mode is on.")
    print("________________________________________________")
    print("You are now starting the Decimal System program.")
    print("Please input the values of the numbers you want to add:")
    print("Do not forget the decimal and the number that comes after it!")
    a = input("The value of the first number is:")
    b = input("The value of the second number is:")
    # variables
    global a_period
    global b_period
    global a_num_1
    global b_num_1
    global a_num_2
    global b_num_2
    global a_num
    global b_num
    a_period = False
    b_period = False
    a_num_1 = False
    b_num_1 = False
    a_num_2 = False
    b_num_2 = False
    a_num = ""
    b_num = ""
    # A:
    a_start = 0
    # ^ this one is how many numbers before decimal
    a_string_count = 0
    # ^ this one is how many numbers there are in "A"
    a_string_list = []
    # ^ this one is the numbers seperated into a string
    # ______________________________________________
    # this "for" loop finds the length of the string
    # and the amount of numbers before decimal
    for i in a:
        if a_num_1 is False:
            if i == "0":
                # ^ checking if 0
                continue
            else:
                a_num_1 = True
            # ^ if it isnt 0
        if a_period is False:
            if a_num_1 is True:
                a_start += 1
        if i != ".":
            a_string_list.append(int(i))
            a_string_count += 1
        else:
            a_period = True
    a_start -= 1
    a_multiplier = 10 ** a_start / 10
    # just some nice displays
    if debug is True:
        print("A:")
        print("length:", a_string_count)
        print("amount before decimal:", a_start)
        print("multiplier Start:", a_multiplier)
        print("list:", a_string_list)
    # _________________________________________________________________________________________
    # B:
    b_start = 0
    # ^ this one is how many numbers before decimal
    b_string_count = 0
    # ^ this one is how many numbers there are in "B"
    b_string_list = []
    # ^ this one is the numbers seperated into a string
    # ______________________________________________
    # this "for" loop finds the length of the string
    # and the amount of numbers before decimal
    for i in b:
        if b_num_1 is False:
            if i == "0":
                # ^ checking if 0
                continue
            else:
                b_num_1 = True
            # ^ if it isnt 0
        if b_period is not True:
            if b_num_1 is True:
                b_start += 1
        if i != ".":
            b_string_list.append(int(i))
            b_string_count += 1
        else:
            b_period = True
    b_start -= 1
    b_multiplier = 10 ** b_start / 10
    # define archives
    a_multiplier_archive = a_multiplier
    b_multiplier_archive = b_multiplier
    # just a nice display
    if debug is True:
        print("B:")
        print("length:", b_string_count)
        print("amount before decimal:", b_start)
        print("multiplier Start:", b_multiplier)
        print("list:", b_string_list)

    # now we do the math
    # __________________
    # "A" math:
    item_num = 0
    if debug is True:
        print("A:")
        print("length:", a_string_count)
        print("list:", a_string_list)
    while item_num < a_string_count:
        a_num = a_multiplier * a_string_list[item_num]
        # ^ this multiplys the first number of "A" by its place
        a_string_list.pop(item_num)
        a_string_list.insert(item_num, round(a_num, item_num))
        item_num += 1
        a_multiplier /= 10
    if debug is True:
        print("A:")
        print("length:", a_string_count)
        print("list:", a_string_list)

    # "B" math:
    item_num = 0
    if debug is True:
        print("B:")
        print("length:", b_string_count)
        print("list:", b_string_list)
    while item_num < b_string_count:
        b_num = b_multiplier * b_string_list[item_num]
        # ^ this multiplys the first number of "B" by its place
        b_string_list.pop(item_num)
        b_string_list.insert(item_num, round(b_num, item_num))
        item_num += 1
        b_multiplier /= 10
        if debug is True:
            print("B:")
            print("length:", b_string_count)
            print("list:", b_string_list)

    # add numbers function

    def add_numbers():
        if debug is True:
            print("A:")
            print("length:", a_string_count)
            print("First multiplier:", a_multiplier_archive)
            print("list:", a_string_list)
            print("B:")
            print("length:", b_string_count)
            print("First multiplier:", b_multiplier_archive)
            print("list:", b_string_list)
        item_num = 0
        # ^ defining how many times to repeat
        result_list = []
        result_num = 0
        result = ""

        while item_num != a_string_count:
            # ^ this loop is for adding the numbers
            result_num = a_string_list[item_num] + b_string_list[item_num]
            result_list.append(result_num)
            item_num += 1
            if debug is True:
                print("list:", result_list)
        item_num = 0
        if debug is True:
            print("list:", result_list)

        while item_num < (a_string_count - 1):
            # ^ this loop is for supplying an answer
            result = result_list[0] + result_list[1]
            del result_list[0:2]
            result_list.insert(0, result)
            item_num += 1
            if debug is True:
                print("result:", result_list, result)
        print("Answer to", a, "+", b, "is", result)
        print(a, "+", b, "=", result)
        pause = input("Hit enter to continue.")
        count = 0
        while count <= 100:
            print("")
            count += 1
        print("Hello! Thank you for choosing the decimal system program.")
        print("Please type \"Debug\" or \"Start\" and hit enter.")
        print("By default Debug is off.")
        print("Turns out you can just use \"float()\" to do this :(")
        menu()

    # remove 0s from end of a
    item_num = (a_string_count - 1)
    while item_num != 0:
        if a_num_2 is False:
            if a_string_list[item_num] == 0:
                a_string_list.pop(item_num)
                item_num -= 1
                a_string_count -= 1
            else:
                a_num_2 = True
        else:
            break
        if debug is True:
            print("A stuff:", item_num, b_string_count, b_string_list)

    # remove 0s from end of b
    item_num = (b_string_count - 1)
    while item_num != 0:
        if b_num_2 is False:
            if b_string_list[item_num] == 0:
                b_string_list.pop(item_num)
                item_num -= 1
                b_string_count -= 1
            else:
                b_num_2 = True
        else:
            break
        if debug is True:
            print("B stuff:", item_num, b_string_count, b_string_list)

    # equal the numbers out
    while (a_multiplier_archive != b_multiplier_archive):
        if debug is True:
            print("A 1:", a_string_count, a_multiplier_archive, a_string_list)
            print("B 1:", b_string_count, b_multiplier_archive, b_string_list)
        if a_multiplier_archive < b_multiplier_archive:
            a_multiplier_archive *= 10
            a_string_list.insert(0, (int(0) * a_multiplier_archive))
            a_string_count += 1
        else:
            b_multiplier_archive *= 10
            b_string_list.insert(0, (int(0) * b_multiplier_archive))
            b_string_count += 1
        if debug is True:
            print("A 1:", a_string_count, a_multiplier_archive, a_string_list)
            print("B 1:", b_string_count, b_multiplier_archive, b_string_list)
        if a_multiplier_archive == b_multiplier_archive:
            break

    # make sure counts are same length
    while a_string_count != b_string_count:
        if debug is True:
            print("A 2: ", a_string_count, a_multiplier_archive, a_string_list)
            print("B 2: ", b_string_count, b_multiplier_archive, b_string_list)
        if a_string_count < b_string_count:
            a_string_count += 1
            a_string_list.append(int(0))
        else:
            b_string_count += 1
            b_string_list.append(int(0))
        if a_string_count == b_string_count:
            break
    add_numbers()
# menu
print("Hello! Thank you for choosing the decimal system program.")
print("Please type \"Debug\" or \"Start\" and hit enter.")
print("By default Debug is off.")
print("Turns out you can just use \"float()\" to do this :(")
def menu():
    global debug
    choice = input()
    if choice == "Debug":
        if debug is True:
            debug = False
            print("Debug is off now.")
            print("Please type \"Debug\" or \"Start\" and hit enter.")
            menu()
        else:
            debug = True
            print("Debug is on now.")
            print("Please type \"Debug\" or \"Start\" and hit enter.")
            menu()
    elif choice == "Start":
        decimal_system()
    else:
        print("I don't know what your typing.")
        print("Please type \"Debug\" or \"Start\" and hit enter.")
        menu()
menu()