name = "Fionna Flynn"
print(">> name is:", name)
newName = name.upper()
print(">> name now is:", name)
print(">> name now is:", newName)

quotes = """Work Hard, Get Luckier
 Serch the Candle, rather than cursing the darkness
 """

def count(data, word, start, end):
    c = 0
    j = 0
    for i in range(start, end):
        print(data[i] == word[j])
        j+=1
        i+=j

     return c

print(">> the occurs:", count(quotes, "the", 0, len(quotes)))

