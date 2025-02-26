#Task 2: Python Control Structures Challenge
def check_even_odd(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("Enter an integer: "))
print(f"The number {num} is {check_even_odd(num)}.")

even_numbers = [i for i in range(1, 51) if i % 2 == 0]
print("Even numbers from 1 to 50:", even_numbers)

count = 10
while count >= 1:
    print(count)
    count -= 1
