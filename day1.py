import random
rnumber = random.randint(1, 100)

count = 1
tf = True


while tf:

    number = int(input("Enter the number : " ))
    if number == rnumber:
        print("Good")
        print(f"You tried {count} times")
        tf = False
    elif number < rnumber:
        print("Its low!")
        count = count +1
    elif number > rnumber:
        print("Its high!")
        count = count +1