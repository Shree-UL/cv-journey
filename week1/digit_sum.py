num = int(input("Enter a number:"))
total = 0
while num != 0:
    total = total + (num % 10)
    #print(total)
    num = num // 10
    #print(num)

print(total)