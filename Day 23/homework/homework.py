# დავალება 1
def func(x, y):
    if type(x) and type(y) != str:
        return int(x) + int(y)
    else:
        return x + y

print(func("3", 6))

# დავალება 2

def func(x, i):
    x = int(x)
    y = int(i)
    if x == 0 or y == 0:
        print("ZeroDivissionError")
    elif x > y:
        print(x / y)
    elif y > x:
        print(y / x)
    else:
        print(y + x)

print(func(5, 10))


# 3 დავალება

def combine_func(x):
    string = ""
    number = ""
    for i in x:
        if type(i) == int:
            number += str(i) + " "
        else:
            string += str(i) + " "
    return string + number

print(combine_func("Hello", 123, "!", 43))

# 4 დავალბეა

def check(y, x):
    if type(y) == x:
        return True
    else:
        return False
print(check("Goa", str))
