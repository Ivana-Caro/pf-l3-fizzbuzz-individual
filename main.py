    
100 % 5   # 0  → 100 is divisible by 5
100 % 3   # 1  → 100 is not divisible by 3   

10 % 5   # 0  → 10 is divisible by 5
10 % 3   # 1  → 10 is not divisible by 3   
for number in range(1, 1001):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
