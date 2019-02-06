text = input()

text_ar = text.split(' ')

def plus(text):
    try:
        print(text[1], text[0], text[2], "=", int(text[1]) + int(text[2]))
    except IndexError:
        print("Insufficient number of arguments passed")
    except ValueError:
        print("One of the values was passed incorrectly")

def mines(text):
    try:
        print(text[1], text[0], text[2], "=", int(text[1]) - int(text[2]))
    except IndexError:
        print("Insufficient number of arguments passed")
    except ValueError:
        print("One of the values was passed incorrectly")

def multiply(text):    
    try:
        print(text[1], text[0], text[2], "=", int(text[1]) * int(text[2]))
    except IndexError:
        print("Insufficient number of arguments passed")
    except ValueError:
        print("One of the values was passed incorrectly")

def divide(text):
    try:
        print(text[1], text[0], text[2], "=", int(text[1]) / int(text[2])) 
    except IndexError:
        print("Insufficient number of arguments passed")
    except ValueError:
        print("One of the values was passed incorrectly")
    except ZeroDivisionError:
        print(text[1], text[0], text[2], "= 0")

if (text_ar[0] == '+'):
    plus(text_ar)
    
if (text_ar[0] == '-'):
    mines(text_ar)
    
if (text_ar[0] == '*'):
    multiply(text_ar)
    
if (text_ar[0] == '/'):
    divide(text_ar)
