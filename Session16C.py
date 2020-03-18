file = open("Session15.py", "r")
line1 = file.readline()
print(line1)
line2 = file.readline()
print(line2)
line3 = file.readline()
print(line3)

lines = file.readlines()
print(type(lines))

functions = 0
for line in lines:
    if "def" in line:
        print(line)
        functions += 1

print(">> Total Functions:", functions)