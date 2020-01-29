def square(num):
    print(">> [SQUARE] num is:", num, hex(id(num)))
    num = num * num
    print(">> [SQUARE] num now is:", num, hex(id(num)))


num = 10
print(">> [MAIN] num is:", num, hex(id(num)))
square(num)
print(">> [MAIN] num now is:", num, hex(id(num)))
