# 1)  მომხმარებელს შემოატანინეთ სამი რიცხვი და გამოიტანეთ ამ რიცხვების ჯამი

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

result = num1+num2+num3

print(result) 

# 2) შემოატანინეთ მომხმარებელს სახელი და შეინახეთ მისი სახელი ცვლადში

name = input("Enter your name: ")



# 3) შემოიტანინეთ მომხმარელს ორი რიცხვი, თუ პირველი რიცხვი მეტია მეორეზე გამოიტანეთ True ( boolean ) თუ არადა გამოიტანეთ False ( boolean )

num4 = int(input("Enter first number: "))
num5 = int(input("Enter second number: "))

result1 = (num4>num5)

print(result1)


# 4) მომხმარებელს შემოვატანინოთ სიტყვა და n რიცხვი, შემდეგ გამოვიტანოთ ეს სიტყვა n-ჯერ.


word = input("Enter your word: ")
num6 = int(input("Enter number: "))

print(word * num6)

# 5) შემოაყვანინეთ მომხმარებელს ორი რიცხვი, და გამოპრინტეთ ამ ორი რიცხვის გაერთიანებულ ვერსისას დამატებული 1, მაგ თუ ჯერ შემოვიდა ათი შემდეგ 11, თქვენი მიზანია გამოიტანოთ 1012, ვინაიდან 10 გაერთანებული 11 არის 1011 და 1011 + 1 არის 1012

num7 = input("Enter first number: ")
num8 = input("Enter second number: ")

result1 = (num7 + num8)


num9 = int(result1) + 1

print(num9)




