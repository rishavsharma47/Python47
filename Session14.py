class CA:
    # In Python, OVERLOADING is not supported
    def __init__(self):
        print(">> CA Object Constructed")

    def __int__(self, num):
        print(">> CA object constructed and num is", num)

cRef = CA()