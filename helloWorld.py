# Hello World lab
print("Hello, world")

num2 = 5

while True:
    try:
        print("Please give me a number to add to 5")
        num1 = int(input())
    except ValueError:
        print("Please put a valid number")
        continue
    else:
        break
        
print(num1 + num2)