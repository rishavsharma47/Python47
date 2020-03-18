
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("private_key.json")
firebase_admin.initialize_app(cred)
print("Firebase Configured and Initialize")

class Customer:

    def __init__(self):
            self.name = input("Enter Customer Name: ")
            self.phone = input("Enter Customer Phone: ")
            self.email = input("Enter Customers Email: ")

    def showCustomerDetails(self):
        print("{} | {} | {}".format(self.name, self.phone, self.email))



# APPLICATION :)
def main():

    db = firestore.client()

    """
    customer = Customer()
    customer.showCustomerDetails()

    customerData = customer.__dict__
    print(customerData, type(customerData))

    db = firestore.client()
    db.collection("customers").document(customer.email).set(customerData)
    print(">> CUSTOMER SAVED")
    """

    docRef = db.collection("customers").document("john.watson@example.com").get()
    docDict = docRef.to_()
    print(docDict)
    cRef = Customer()
    cRef.name = docDict["name"]
    cRef.phone = docDict["phone"]
    cRef.email = docDict["email"]

    cRef = showCustomerDetails()


if __name__ == "__main__":
    main()