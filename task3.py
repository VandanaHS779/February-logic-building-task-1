# Problem 1: Employee Performance Bonus Eligibility

employees = {
    "Ravi": 92,
    "Anita": 88,
    "Kiran": 92,
    "Suresh": 85
}

# Find the highest performance score
highest_score = max(employees.values())

# Find all employees who have the highest score (handle ties)
top_performers = [name for name, score in employees.items() if score == highest_score]

# Display result
print("Top Performers Eligible for Bonus:", ", ".join(top_performers), f"(Score: {highest_score})")


# Problem 2: Search Query Keyword Analysis

import string

query = "Buy mobile phone buy phone online"

# Convert to lowercase
query = query.lower()

# Remove punctuation
query = query.translate(str.maketrans('', '', string.punctuation))

# Split into words
words = query.split()

# Count frequency
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Display words searched more than once
result = {word: count for word, count in word_count.items() if count > 1}

print(result)




# Problem 3: Sensor Data Validation

sensor_readings = [3, 4, 7, 8, 10, 12, 5]

valid_readings = []

# Check for even readings and store (index, value)
for index, value in enumerate(sensor_readings):
    if value % 2 == 0:  # Even number check
        valid_readings.append((index, value))

print("Valid Sensor Readings (Hour, Value):")
print(valid_readings)



# Problem 4: Email Domain Usage Analysis

emails = [
    "ravi@gmail.com",
    "anita@yahoo.com",
    "kiran@gmail.com",
    "suresh@gmail.com",
    "meena@yahoo.com"
]

domain_count = {}

# Extract domain and count
for email in emails:
    domain = email.split("@")[1]
    domain_count[domain] = domain_count.get(domain, 0) + 1

total_emails = len(emails)

# Calculate and display percentage
for domain, count in domain_count.items():
    percentage = (count / total_emails) * 100
    print(f"{domain}: {percentage:.0f}%")




# Problem 5: Sales Spike Detection

sales = [1200, 1500, 900, 2200, 1400, 3000]

# Calculate average sales
average_sales = sum(sales) / len(sales)

# Detect spikes (> 30% above average)
threshold = average_sales * 1.30

for index, value in enumerate(sales):
    if value > threshold:
        print(f"Day {index + 1}: {value}")




# Problem 6: Duplicate User ID Detection

user_ids = ["user1", "user2", "user1", "user3", "user1", "user3"]

id_count = {}

# Count occurrences
for user in user_ids:
    id_count[user] = id_count.get(user, 0) + 1

# Display duplicates only
for user, count in id_count.items():
    if count > 1:
        print(f"{user} → {count} times")
