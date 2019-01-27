text = input()

text_ar = text.split(' ')

if (text_ar[0] == '+'):
    try:
        try:
            print(text_ar[1], text_ar[0], text_ar[2], "=", int(text_ar[1]) + int(text_ar[2]))
        except IndexError:
            print("Insufficient number of arguments passed")
    except ValueError:
        print("One of the values was passed incorrectly")

if (text_ar[0] == '-'):
    try:
        try:
            print(text_ar[1], text_ar[0], text_ar[2], "=", int(text_ar[1]) - int(text_ar[2]))
        except IndexError:
            print("Insufficient number of arguments passed")
    except ValueError:
        print("One of the values was passed incorrectly")
if (text_ar[0] == '*'):
    try:
        try:
            print(text_ar[1], text_ar[0], text_ar[2], "=", int(text_ar[1]) * int(text_ar[2]))
        except IndexError:
            print("Insufficient number of arguments passed")
    except ValueError:
        print("One of the values was passed incorrectly")

if (text_ar[0] == '/'):
    try:
        try:
            try:
                print(text_ar[1], text_ar[0], text_ar[2], "=", int(text_ar[1]) / int(text_ar[2])) 
            except IndexError:
                print("Insufficient number of arguments passed")
        except ValueError:
            print("One of the values was passed incorrectly")
    except ZeroDivisionError:
        print(text_ar[1], text_ar[0], text_ar[2], "= 0")
