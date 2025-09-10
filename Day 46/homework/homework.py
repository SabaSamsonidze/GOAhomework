# 1st homework
def funcsum(num, num1):
    return num + num1

print(funcsum(51, 23))

# 2nd homework
def funcpower(number):
    return number ** 2

print(funcpower(5))

# 3rd homework

def funcmax(lst):
    lst == []
    return max(lst)

print(funcmax([5, 2, 9]))

# 4th homework

def funcaverage(a, b, c):
    return (a + b + c) / 3

print(funcaverage(4, 5, 1))

# 5th homework

def lstreverse(lst1):
    return lst1[::-1]

print(lstreverse([1, 2, 3]))

# 6th homework

def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    
print(palindrome("saba"))