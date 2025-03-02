# 1 დავალება
for i in range (2, 26):
   if i % 2 != 0:
        print(i)

# 2 დავალება

name = input("please enter your name: ")
for i in name:
    print(i)


# 3 დავალება 

correct_password = "Pass123"
password_guess = input("Please input a password: ")
while password_guess != correct_password:
    password_guess = input("wrong password try again: ")

print("Correct password")













