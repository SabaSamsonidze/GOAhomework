# 1 დავალება
num = int(input("შეიყვანეთ სამნიშნა რიცხვი: "))

hundreds = num // 100
tens = num // 10 % 10
ones = num % 10

digit_sum = hundreds + tens + ones

remainder = num % digit_sum

print(remainder)

# 2 დავალება
num = int(input("Enter number here: "))
num += num % 2
print(num)

# 3 დავალება

num = int(input("შეიყვანეთ მთელი რიცხვი: "))
if num % 2 == 0:
    num += 5
else:
    num *= 3
result = num % 5
print(result)

# 4 დავალება

name = input("Enter your name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
country = input("Enter your country: ")
result = f"Hello {name} {last_name}, your {age} years old and you live in {country}"
print(result)

# 5 დავალება, დავალების პირობა: ახსენით რომელი გირჩევნიათ და რატომ

num = 2
print("Hello " + str(num) + " world")
print("Hello", num, "world")
print(f'Hello {num} world')

# პასუხი:₾ მე მირჩევნია მესამე ვარიანტი, რადგან კოდი უფრო მარტივად იწერება და ადვილად წასაკითხია