def num():
    a = input("Number to sort through:")
    # A:
    a_string_count = 0
    # ^ this one is how many numbers there are in "A"
    a_count = 0
    # ^ this is how many 0s there are
    b_count = 0
    # ^ this is how many 1s there are
    c_count = 0
    # ^ this is how many 2s there are
    d_count = 0
    # ^ this is how many 3s there are
    e_count = 0
    # ^ this is how many 4s there are
    f_count = 0
    # ^ this is how many 5s there are
    g_count = 0
    # ^ this is how many 6s there are
    h_count = 0
    # ^ this is how many 7s there are
    i_count = 0
    # ^ this is how many 8s there are
    j_count = 0
    # ^ this is how many 9s there are
    a_string_list = []
    # ^ this one is the numbers seperated into a string
    # ______________________________________________
    # this "for" loop finds the length of the string
    # and the amount of numbers before decimal
    for i in a:
        if i == "0":
            a_count += 1
        elif i == "1":
            b_count += 1
        elif i == "2":
            c_count += 1
        elif i == "3":
            d_count += 1
        elif i == "4":
            e_count += 1
        elif i == "5":
            f_count += 1
        elif i == "6":
            g_count += 1
        elif i == "7":
            h_count += 1
        elif i == "8":
            i_count += 1
        elif i == "9":
            j_count += 1
        elif i != ".":
            a_string_count += 1
        else:
            if i == ".":
                continue
            else:
                print("You made a mistake inputting the string, please change it:")
                print("Old input:", a)
                a = input("New input:")
    print("0:", a_count)
    print("1:", b_count)
    print("2:", c_count)
    print("3:", d_count)
    print("4:", e_count)
    print("5:", f_count)
    print("6:", g_count)
    print("7:", h_count)
    print("8:", i_count)
    print("9:", j_count)
    pause = input("Press enter to continue.")
    num()
num()