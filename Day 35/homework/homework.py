# homework 1
correct_password = "saba12"
user_password = input("Enter password: ")

while user_password != correct_password:
    user_password = input("Enter password: ")

print("Logged in")

# homework 2

def remove_smallest(numbers):
    if numbers == []: return []

    nums = []
    for i in numbers: nums.append(i)

    min_index = nums.index(min(nums))
    nums.pop(min_index)

    return nums

# homework 3

def remove_smallest(numbers):
    # თუ სია ცარიელია, დააბრუნე ცარიელი სია
    if numbers == []:
        return []

    # შევქმნათ ახალი სია იგივე ელემენტებით
    nums = []
    for i in numbers:
        nums.append(i)

    # ვიპოვოთ ყველაზე პატარა ელემენტის ინდექსი
    min_index = nums.index(min(nums))

    # ამოვშალოთ ეს ელემენტი სიიდან
    nums.pop(min_index)

    # დავაბრუნოთ მიღებული სია
    return nums


