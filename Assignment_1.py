#exercise 1
name = "Bob"
student_number = "ST1001"
email_address = "bob@gmail.com"

print (name, student_number, email_address)

#exercise 2
print("Name: Bob\nStudent Number: ST1001\nEmail Address: bob@gmail.com")

#exercise 3
num1 = 14
num2 = 7

print(num1, "+", num2, "=", num1 + num2)
print(num1, "*", num2, "=", num1 * num2)
print(num1, "-", num2, "=", num1 - num2)
print(num1, "/", num2, "=", num1 / num2)

#exercise 4

for i in range(1, 6):
    print(i)

#exercise 5
print('An example runs of the program: "SDK" stands for "Software Development Kit", whereas "IDE" stands for "Integrated Development Environment"')

#exercise 6
print("python is an \"awesome\" language.")
print("python\n\t2023")
print('I\'m from Entri.\b')
print("\65")
print("\x65")
print("Entri", "2023", sep="\n")
print("Entri", "2023", sep="\b")
print("Entri", "2023", sep="*", end="\b\b\b\b")

#exercise 7

num = 23
print(type(num))

textnum = "57"
print(type(textnum))

decimal = 98.3
print(type(decimal))

sum = num + int(textnum) + decimal
print(sum)
print(type(sum))

#exercise 8

# Define variables for each unit of time
days_in_year = 365
hours_in_day = 24
minutes_in_hour = 60

# Calculate total minutes in a year
total_minutes_in_year = days_in_year * hours_in_day * minutes_in_hour

# Print the result
print("This code calculates the total number of minutes in a year.")
print("There are", total_minutes_in_year, "minutes in a year.")

#exercise 9
name = input("Please enter your name: ")
print("Hi", name, " welcome to Python programming ")

#exercise 10
# Ask the user to enter an amount in pounds
pounds = float(input("Please enter amount in pounds: £"))

# Conversion rate (1 pound = 1.31 dollars)
conversion_rate = 1.31

# Calculate the amount in dollars
dollars = pounds * conversion_rate

# Print the result
print(f"{pounds} £ are ${dollars:.2f}")






















