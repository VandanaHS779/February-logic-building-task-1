 # Given credentials
username = "admin"
password = "1234"

# Input credentials (example)
input_username = "admin"
input_password = "1234"

# Login check
if input_username == username and input_password == password:
    print("Login Successful")
else:
    print("Invalid Credentials")


marks = [45, 78, 90, 33, 60]

pass_count = 0
fail_count = 0

for mark in marks:
    if mark >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("Total Pass Students:", pass_count)
print("Total Fail Students:", fail_count)


names = [" Alice ", "bob", " CHARLIE "]

cleaned_names = []

for name in names:
    cleaned_name = name.strip().lower()
    cleaned_names.append(cleaned_name)

print("Cleaned Names:", cleaned_names)


messages = ["Hi", "Welcome to the platform", "OK"]

for message in messages:
    length = len(message)
    print(f"Message: '{message}' | Length: {length}")
    
    if length > 10:
        print("-> This message is longer than 10 characters")



logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

for log in logs:
    if log == "ERROR":
        error_count += 1

print("Total ERROR entries:", error_count)


