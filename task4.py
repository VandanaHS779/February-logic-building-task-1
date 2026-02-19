def validate_recharge(amount):
    valid_plans = [199, 299, 399, 599]

    if amount < 50:
        print("Recharge amount must be at least ₹50")
        return False
    elif amount not in valid_plans:
        print("Invalid plan selected")
        return False
    else:
        print("Recharge Successful ✅")
        return True


# Retry using while loop
while True:
    amount = int(input("Enter recharge amount: "))
    if validate_recharge(amount):
        break
    print("Please try again...\n")



def check_inventory(products):
    for product, stock in products.items():
        if stock < 15:
            print(f"{product} → Reorder Alert ⚠")
        else:
            print(f"{product} → Stock OK ✅")


# Example data
inventory = {
    "Laptop": 20,
    "Mouse": 10,
    "Keyboard": 8,
    "Monitor": 25
}

check_inventory(inventory)




def process_result(marks):
    total = 0

    for mark in marks:
        total += mark

    average = total / len(marks)

    if average >= 50:
        return f"Average: {average} → Pass ✅"
    else:
        return f"Average: {average} → Fail ❌"


# Example usage
marks_list = [60, 45, 70, 55]
print(process_result(marks_list))




def calculate_fare(distance, peak):
    base_fare = 50
    fare = base_fare + (12 * distance)

    if peak.lower() == "yes":
        fare += fare * 0.25

    return fare


while True:
    distance = float(input("Enter distance in km: "))
    peak = input("Is it peak hour? (yes/no): ")

    total_fare = calculate_fare(distance, peak)
    print(f"Total Fare: ₹{total_fare}")

    retry = input("Do you want to calculate again? (yes/no): ")
    if retry.lower() != "yes":
        break




def check_eligibility(attendance):
    present_days = 0

    for day in attendance:
        if day == "P":
            present_days += 1

    percentage = (present_days / len(attendance)) * 100

    if percentage >= 75:
        return f"Attendance: {percentage}% → Eligible ✅"
    else:
        return f"Attendance: {percentage}% → Not Eligible ❌"


# Example usage
attendance_list = ["P", "P", "A", "P", "P", "A", "P", "P"]
print(check_eligibility(attendance_list))




def check_password(password):
    has_digit = False
    has_special = False
    special_chars = "@#$"

    if len(password) < 8:
        return "Weak Password ❌ (Minimum 8 characters required)"

    for char in password:
        if char.isdigit():
            has_digit = True
        if char in special_chars:
            has_special = True

    if has_digit and has_special:
        return "Strong Password ✅"
    else:
        return "Weak Password ❌ (Must include digit and special character)"


# Example usage
user_password = input("Enter password: ")
print(check_password(user_password))
