third_loop = 65
for first_loop in range(int(input('Enter the number of rows: '))):
    string = ''
    for second_loop in range(first_loop + 1):
        string += chr(third_loop)
        third_loop +=1
        if (third_loop == (65 + 26)) : third_loop = 65
    print(string)