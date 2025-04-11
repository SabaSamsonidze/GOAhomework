# 1 დავალება

numbers = [1, 4, 3, 6, 9, 11, 17, 13, 26, 30]

even_sum = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_count += 1

print("sum of even numbers:", even_sum)
print("number of odd numbers:", odd_count)

# 2 დავალება

list = [1, 3, 5,]
list.append(6)
print(list)

# 3 დავალება

list = [1,2,3,3,4,5]
list.pop(2)
print(list)

# 4 დავალება

list = [1, 2, 3, 4, 8, 9]

list.insert(4, 5)
list.insert(5, 6)
list.insert(6, 7)

print(list)

# 5 დავალება

# append – ამატებს ელემენტს სიას ბოლოში
# pop – შლის ელემენტს კონკრეტული ინდექსიდან (თუ არ მივუთითებთ, შლის ბოლო ელემენტს)
# insert – ამატებს ელემენტს სიაში მითითებულ ინდექსზე

