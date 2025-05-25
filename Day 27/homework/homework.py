#1)
day1 = int(input("enter day: "))
month1 = int(input("enter month: "))
year1 = int(input("enter year: "))

print(f"{day1}/{month1}/{year1}")

#2)
password = input("enter a password: ")

if len(password) < 8:
    print("password is too short")
else:
    print("password is confirmed")

#3)
num1 = int(input("enter a num: "))
num2 = int(input("enter a num: "))
num3 = int(input("enter a num: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)

#4)
num4 = int(input("enter a num: "))
num5 = int(input("enter a num: "))
num6 = int(input("enter a num: "))
num7 = int(input("enter a num: "))
num8 = int(input("enter a num: "))

lst1 = [num4,num5,num6,num7,num8]

print(sum(lst1))