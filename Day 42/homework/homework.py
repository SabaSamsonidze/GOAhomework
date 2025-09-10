# homework 1

# Mutable - ობიექტი, რომლის შემცველობის შეცვლა შეიძლება ( напр. list)
# Immutable - ობიექტი, რომლის შემცველობის შეცვლა შეუძლებელია ( напр. string)

# Mutable ობიექტი იცვლება იგივე ადგილას მეხსიერებაში
# Immutable ობიექტის "შეცვლა" ქმნის ახალ ობიექტს

# Mutable = ცვალებადი
# Immutable = უცვლელი


# homework 2

lst1 = [1, 2, 4, 5]

print(lst1[2])
print(lst1[2:-1])


# homework 3

# if statement

text = "Hello world"

if text[:5] == "Hello":
    print("დასაწყისში არის 'Hello'")

# for loop

numbers = [1, 2, 3, 4, 5, 6]
 
for n in numbers[2:5]:
    print(n)

# while loop

i = 0

word = "Python"
while word[i:] != "":
    print(word[i])
    i += 1
