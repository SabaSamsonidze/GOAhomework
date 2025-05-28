# 1 დავალება
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined_list = []

for i in list1:
    combined_list.append(i)

for i in list2:
    combined_list.append(i)

print(combined_list)

# 2 დავალება
def remove_odds(numbers):
    even_numbers = []
    for i in numbers:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

nums = [5, 9, 33, 20, 21]
print(remove_odds(nums))

# 3 დავალება
def join_number(number):
    result = ""
    for i in number:
        result += str(i)
    return result

nums = [1, 4, 6, 21]
print(join_number(nums))