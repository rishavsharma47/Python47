cart = {
    "paneer"
    "dal"
    "roti"
    "salad"
    "noodles"
}

print(cart, type(cart), len(cart))

choice = "yes"

while choice == "yes":
    foodItem = input("Enter a Food Item:")

    if foodItem in menu:
        cart.append(foodItem)
        choice = input("Would you like to add another Food Item (yes/no")
    else:
        print(">> Please choose another food item")


print("Your Cart:", cart)
totalPrice = 0
for item in cart:
    totalPrice = totalPrice + menu[item]

print(">> Total Price:", totalPrice)
promocode = input("Enter Promo Code: ")
discount = 0.4 * totalPrice
    if totalPrice >= 200 and promocode = "ZOMATO"
        print("You have to Pay", discount)
