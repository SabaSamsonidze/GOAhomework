# 1 დავალება

for i in range(1, 51):
    num = int(input("Enter a number (1-50): "))
    if 1 <= num <= 50:
        break
    print("Please enter a number (1-50)")

print( str(num) + " " + "multiples up to and including 100")
for i in range(num, 101, num):
    print(i)

# 2 დავალება

correct_number = 4323  

print("Hey let's play a number guessing game")
print("I have chosen a random number in my head try to guess it correctly! hint: its four digits")

while True:
    guess = int(input("Enter your guess (4-digit number): "))
    
    if guess == correct_number:
        print("Wow congratulations, you actually guessed it correctly, that probably took a lot of tries.")
        break
    elif guess < correct_number:
        print("Wrong, you should probably go higher")
    else:
        print("Wrong, Maybe go lower")
