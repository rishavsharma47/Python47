print(">> Welcome to Python App")

num = 5
print(">> 1. num is:", num)

def square(n):
    global num
    n = n*n
    num = n
    print(">> 2. n is:", n)
    print(">> 3. num is:", num)

square(7)
print(">. 4. num is:", num)