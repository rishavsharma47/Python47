
salutation = "Mr."
fname = "George"

name = salutation + fname
print(">> name:", name)
print(">> salutation:", salutation)

number = "100"
print(">> number:",number, type(number))
print(">> is digit:", number.isdigit())

songName = "Hello.mp3"
if songName.endswith(".mp3"):
    print(">> We can play this audio file")
else:
    print(">> Invalid audio format")
