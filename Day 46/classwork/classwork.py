# classwork 1

def funcmax(num, num1, num2):
    return max(num, num1, num2)

print(funcmax(5, 4, 2))

# classwork 2

def funclen(word):
    return len(word)

print(funclen("saba423"))

# classwork 3

def funcpower(num):
    return num ** 2

print(funcpower(4))

# classwork 4

def funcmultiply(num1, num2, num3):
    return num1 * num2 * num3

print(funcmultiply(2, 5, 3))

# classwork 5

def funcnegpos(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    elif num == 0:
        return "Zero"
    
print(funcnegpos(0))