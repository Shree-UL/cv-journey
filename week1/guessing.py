import random
actual_num = random.randint(1,20)
counter = 0
while True:
    
    guessed_num = int(input("Guess the number between 1 - 20: "))
    counter = counter + 1
    if guessed_num == actual_num:
        print("Hurrayyy!, you guessed in :", counter)
        break
    
    if guessed_num > actual_num:
        print("Lower")
    
    if guessed_num < actual_num:
        print("Higher")