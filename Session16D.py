file = open("Session15.py", "r")

print(file.tell())

# Move Cursor Location
file.seek(10)
data = file.read(15)
print(data)

# Tell Cursor Location
print(file.tell())