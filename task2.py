sentence = input("Enter sentence: ")

words = sentence.split()          # Split into words
unique_words = set(words)         # Remove duplicates

print("Unique words count:", len(unique_words))
print("Unique words:", unique_words)



employees = {
    "Ravi": 75000,
    "Anita": 68000,
    "Kiran": 72000
}

highest_employee = max(employees, key=employees.get)
highest_salary = employees[highest_employee]

print("Highest Salary:", highest_employee, "-", highest_salary)



numbers = [45, 22, 89, 10, 66]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

print("List:", numbers)
print("Max:", maximum)
print("Min:", minimum)




prices = [450, 1200, 899, 1500, 300]

count = 0
for price in prices:
    if price > 1000:
        count += 1

print("Products above 1000:", count)




attendance = ["P", "P", "A", "P", "P"]

present_count = attendance.count("P")
total_days = len(attendance)

percentage = (present_count / total_days) * 100

print("Attendance Percentage:", percentage)




phone_numbers = [9876543210, 9123456789, 9876543210]

unique_numbers = set(phone_numbers)

print("Unique phone numbers:", unique_numbers)



text = "python"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)




numbers = [10, 20, 30]

numbers_tuple = tuple(numbers)

print("Tuple:", numbers_tuple)




employees = {
    "Ravi": 75000,
    "Anita": 68000
}

key = "Ravi"

if key in employees:
    print("Employee exists")
else:
    print("Employee does not exist")




marks = [70, 75, 80, 65]

total = sum(marks)
average = total / len(marks)

print("Average Marks:", average)
