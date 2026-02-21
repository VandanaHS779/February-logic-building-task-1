def analyze_engagement(likes):
    total_likes = 0
    for like in likes:
        total_likes += like

    if total_likes >= 1000:
        status = "Viral Post"
    else:
        status = "Normal Engagement"

    print("Total Likes:", total_likes)
    print("Post Status:", status)

# Example
analyze_engagement([200, 300, 250, 300])



def check_medicine_stock(stock):
    if stock < 10:
        status = "Low Stock Alert"
    else:
        status = "Stock Sufficient"

    print("Medicine Stock:", stock)
    print("Status:", status)


# Example
check_medicine_stock(6)



def rainfall_checker(rainfall_data, required_level):
    total = 0
    for rain in rainfall_data:
        total += rain

    average = total / len(rainfall_data)

    if average >= required_level:
        status = "Adequate Rainfall"
    else:
        status = "Inadequate Rainfall"

    print("Average Rainfall:", average)
    print("Rainfall Status:", status)


# Example
rainfall_checker([70, 75, 68, 80], 70)




def detect_duplicates(usernames):
    if len(usernames) != len(set(usernames)):
        result = "Yes"
    else:
        result = "No"

    print("Duplicate Accounts Found:", result)


# Example
detect_duplicates(["user1", "user2", "user3", "user1"])


def check_eligibility(age):
    if age >= 18:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print("Patient Age:", age)
    print("Eligibility Status:", status)


# Example
check_eligibility(21)





def filter_premium_crops(prices):
    premium = []
    for price in prices:
        if price > 2000:
            premium.append(price)

    print("Premium Crops:", premium)


# Example
filter_premium_crops([1500, 2500, 1800, 3200])




def application_health(errors):
    if errors == 0:
        status = "Healthy"
    elif errors <= 5:
        status = "Minor Issues"
    else:
        status = "Critical Issues"

    print("Error Count:", errors)
    print("System Status:", status)


# Example
application_health(7)





def transaction_checker(amount):
    daily_limit = 50000

    if amount <= daily_limit:
        status = "Approved"
    else:
        status = "Rejected"

    print("Transaction Amount:", amount)
    print("Transaction Status:", status)


# Example
transaction_checker(60000)




def attendance_checker(attendance_list):
    total_classes = len(attendance_list)
    attended = 0

    for day in attendance_list:
        if day == 1:
            attended += 1

    percentage = (attended / total_classes) * 100

    if percentage >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible"

    print("Attendance Percentage:", percentage)
    print("Exam Eligibility:", status)


# Example
attendance_checker([1,1,1,0,1,1,1,1,0,1])


def electricity_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 3
    elif units <= 200:
        bill = (100 * 3) + (units - 100) * 5
    else:
        bill = (100 * 3) + (100 * 5) + (units - 200) * 7

    if bill < 500:
        usage = "Low Usage"
    elif bill <= 1500:
        usage = "Moderate Usage"
    else:
        usage = "High Usage"

    return bill, usage


# Example
bill, status = electricity_bill(250)
print("Total Bill:", bill)
print("Usage Status:", status)