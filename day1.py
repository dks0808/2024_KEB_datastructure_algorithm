import random
rnumber = random.randint(1, 100)

count = 1
tf = True
print(rnumber)

while tf:

    number = int(input("Enter the number : " ))
    if number == rnumber:
        print("Good")
        print(f"You tried {count} times")
        tf = False
    elif number < rnumber:
        print(f"{number} is lower than random number!")
        count = count +1
    elif number > rnumber:
        print(f"{number} is higher than random number!")
        count = count +1