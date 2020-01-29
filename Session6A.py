def square(num):
    num = num * num
    print (">> num is:", num)


num = 10
print(">> num is:", num, id(num))
square(num)
print(">> num now is:", num)


