class Customer:

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def showCustomerDetails(self):
        print("Name: {} | Phone: {} | Email: {}".format(self.name, self.phone, self.email))


# Customer can be extended to Driver
class Driver(Customer):

    def __init__(self, name, phone, email, licenseNumber):
        Customer.__init__(self, name, phone, email)
        self.licenseNumber = licenseNumber

    def showDriverDetails(self):
        print("DRIVER DETAILS:")
        self.showCustomerDetails()
        print("LicenseNumber:", self.licenseNumber)


class Cab:

    def __init__(self, regNumber, basePrice):
        self.regNumber = regNumber
        self.basePrice = basePrice

    def showCabDetails(self):
        print("CAB DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))


class OlaMini(Cab):

    def showCabDetails(self):
        print("Ola Mini DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))


class OlaMicro(Cab):

    def showCabDetails(self):
        print("Ola Micro DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))


class OlaSedan(Cab):

    def showCabDetails(self):
        print("Ola Sedan DETAILS:")
        print("RegNum: {} | BasePrice: {}".format(self.regNumber, self.basePrice))


class Ride:
    rideNumber = 1

    def __init__(self, customer):
        self.ride = Ride.rideNumber
        self.customer = customer
        Ride.rideNumber += 1

    def selectSourceAndDestination(self):
        self.source = input("Enter Source: ")
        self.destination = input("Enter Destination: ")
        print("Ride shall be Booked From {} to {}".format(self.source, self.destination))

    def selectCab(self):
        self.cab = None
        print("Select a Cab:")
        print("(MICRO) | (MINI) | (SEDAN)")
        choice = input("Select Type of Cab: ")

        # Run Time Ploymorphism
        if choice == "MICRO":
            self.cab = OlaMicro("PB10AB1234", 100)
        elif choice == "MINI":
            self.cab = OlaMini("PB10CD4568", 200)
        else:
            self.cab = OlaSedan("PB10EF7890", 300)

    def attachDriver(self, driver):
        self.driver = driver

    def showRideDetails(self):
        print("Ride Booked From {} to {}".format(self.source, self.destination))
        print("Ride Number:", self.ride)
        self.cab.showCabDetails()
        self.driver.showDriverDetails()
        self.customer.showCustomerDetails()

    def saveRide(self):
        rideData = "{},{},{},{},{},{},{},{},{},{},{},{}\n".\
            format(self.ride, self.source, self.destination,
                   self.cab.regNumber, self.cab.basePrice,
                   self.driver.name, self.driver.phone, self.driver.email, self.driver.licenseNumber,
                   self.customer.name, self.customer.phone, self.customer.email,
                   )
        print(rideData)

        file = open("rides.csv", "a")
        file.write(rideData)
        file.close()

        print(">> Ride Saved :)")

customer = Customer("John", "+91 98765 98765", "john@example.com")
driver = Driver("Mike", "+91 98709 98090", "mike@example.com", "AB34377XC")

ride = Ride(customer)
ride.selectSourceAndDestination()
ride.selectCab()
ride.attachDriver(driver)
ride.showRideDetails()
ride.saveRide()


# PS: In Program, We have data available in RAM
#     RAM is volatile i.e. temporary.
#     Whenever process will be finished i.e. program is finished data will be LOST
#     Saving Data Somewhere -> Persistence
#     Serialization and De-Serialization | Saving state of an object somewhere and reading the data to create object again