# 1 დავალება
name = input("Enter name here: ")
number = int(input("Enter number here: "))

print(name[number - 1])

# 2 დავალება

for i in range(100, 0, -1):
    print(i)

# 3 დავალება

for i in range(1, 100, 2):
    print (i)

# 4 დავალება

for i in range(250, 500, 10):
    print(i)

# 5 დავალება

word = input("Enter text here: ")

if word == '_':
    print(True)
else:
    print(False)


# 6 დავალება

num = int(input("Enter a number: "))

if num % 2 == 0:
    for i in range (10):
        print("yes")

else:
    print("No")
