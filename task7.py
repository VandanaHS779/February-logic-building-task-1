class SmartLight:
    def __init__(self, name):
        self.name = name
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

    def display_status(self):
        print(f"{self.name} is {self.status}")


# Sample Usage
light = SmartLight("Bedroom Light")
light.turn_on()
light.display_status()

class Employee:
    def __init__(self, name, emp_id, department):
        self.name = name
        self.emp_id = emp_id
        self.department = department

    def display_id_card(self):
        print("Employee ID Card")
        print(f"Name: {self.name}")
        print(f"ID: {self.emp_id}")
        print(f"Department: {self.department}")


# Sample Usage
emp = Employee("Rahul", "EMP102", "IT")
emp.display_id_card()

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def save_contact(self):
        print("Contact Saved")
        print(f"Name: {self.name}")
        print(f"Phone: {self.phone}")


# Sample Usage
contact = Contact("Anita", "9876543210")
contact.save_contact()



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_price_tag(self):
        print(f"Product: {self.name}")
        print(f"Price: ₹{self.price}")


# Sample Usage
product = Product("Headphones", 2499)
product.display_price_tag()



class Movie:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def display_details(self):
        print(f"Movie: {self.name}")
        print(f"Rating: {self.rating} / 5")


# Sample Usage
movie = Movie("Inception", 4.8)
movie.display_details()


class Delivery:
    def __init__(self, customer_name, address):
        self.customer_name = customer_name
        self.address = address

    def display_delivery_details(self):
        print("Delivery Details")
        print(f"Customer: {self.customer_name}")
        print(f"Address: {self.address}")


# Sample Usage
delivery = Delivery("Suman", "Hyderabad")
delivery.display_delivery_details()


