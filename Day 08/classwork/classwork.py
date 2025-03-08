
# 1 დავალება

input_string = input("Enter text here: ")
reversed_string = ""

for i in input_string:
    reversed_string = i + reversed_string

print("Reversed string:", reversed_string)

# 2 დავალება

sum = 0

for i in range(101):
    sum += i

print(sum)

# 3 დავალება 

word = input("Enter 3 letter word: ")

while i in word:
    if len(word) != 3:
        word = input("Wrong Enter 3 letter word: ")
    else:
        if word[0] == word [2]:
            print(True)
            break
        else:
            print(False)
            break   



# 4 დავალება 

for i in range(100, 301):
    square = i * i
    print(square)


# 5 დავალება

for i in range(1000):
    if i % 2 == 0:
        print(False)
    else:
        print(True)



# 6 დავალება


N = int(input("Enter number here: "))

X = N**0.5
print(X)




