
# 1) მომხმარებელს შემოატანინეთ ოთხი რიცხვი და გამოიტანეთ მათი საშუალო არითმეტიკული.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))


result = (num1 + num2 + num3 + num4) / 4

print(result)  # 100 / 4 = 25


# 2) მომხმარებელს შემოატანინეთ სახელი და გვარი, შემდეგ გამოპრინტეთ ტექსტი: „მოგესალმები, [სახელი] [გვარი]!“

first_name = input("Enter name: ")

last_name = input("Enter last name: ")

full_name = "მოგესალმებით, " + first_name + " " + last_name + "!"

print(full_name)

# 3) მომხმარებელს შემოატანინეთ ორი რიცხვი და გამოიტანეთ მათი სტრინგებად გაერთიანებული ვერსია, რომლის შუაშიც იქნება "😊" ემოჯი.

num1 = input("Enter first number: ")

num2 = input("Enter second number: ")

result1 = num1 + "😊" + num2 

print(result1)

