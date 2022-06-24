# coding: utf-8
import csv
from pathlib import Path

"""Part 1: Automate the Calculations."""

loan_costs = [500, 600, 200, 1000, 450]


# Number of loans from the list
number_of_loans = len(loan_costs)
print("The number of loans is:", number_of_loans)


# Total value of the loans

total_loans = sum(loan_costs)
print("the total of all the loans is: $", total_loans)


# Average loan amount

average_loan = total_loans / number_of_loans
print("the average loan amount is: $", average_loan)

"""Part 2: Analyze Loan Data."""

loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Print each variable.

future_value = loan.get("future_value")
print("The future value of the loan is: $", future_value)
remaining_months = loan.get("remaining_months")
print("The remaining months on the loan is: ", remaining_months)

# Formula for Present Value to calculate a "fair value" of the loan.

discount_rate = 0.20
present_value = future_value / (1 + (discount_rate/12)) ** remaining_months
fair_value_of_loan = present_value
print(f"The fair value of the loan is: {fair_value_of_loan: .2f}")


# Conditional statement to decide if the present value represents the loan's fair value.

if present_value < future_value:
    print("Purchase this home!")
else:
    print("Don't buy this home!")


"""Part 3: Perform Financial Calculations."""

new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# A new function that will be used to calculate present value.

def calculate_present_value(future_value, remaining_months, discount_rate):
    present_value = future_value / (1 + (discount_rate/12)) ** remaining_months
    print(f"The present value of the loan is: {present_value: .2f}")
    return present_value


# The function to calculate the present value of the new loan given below.
# An `annual_discount_rate` of 0.2 for this new loan calculation.

calculate_present_value(800, 12, .2)


"""Part 4: Conditionally filter lists of loans.

In this section, you will use a loop to iterate through a series of loans and select only the inexpensive loans.

1. Create a new, empty list called `inexpensive_loans`.
2. Use a for loop to select each loan from a list of loans.
    a. Inside the for loop, write an if-statement to determine if the loan_price is less than or equal to 500
    b. If the loan_price is less than or equal to 500 then append that loan to the `inexpensive_loans` list.
3. Print the list of inexpensive_loans.
"""
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# @TODO: Create an empty list called `inexpensive_loans`
# YOUR CODE HERE!
inexpesnive_loans = []

# @TODO: Loop through all the loans and append any that cost $500 or less to the `inexpensive_loans` list
# YOUR CODE HERE!
for key in loans:
    if loans{"loan_price"} >= 500
        inexpensive_loans.append(loans[])


print(inexpesnive_loans)   


# @TODO: Print the `inexpensive_loans` list
# YOUR CODE HERE!


"""Part 5: Save the results.

Output this list of inexpensive loans to a csv file
    1. Use `with open` to open a new CSV file.
        a. Create a `csvwriter` using the `csv` library.
        b. Use the new csvwriter to write the header variable as the first row.
        c. Use a for loop to iterate through each loan in `inexpensive_loans`.
            i. Use the csvwriter to write the `loan.values()` to a row in the CSV file.

    Hint: Refer to the official documentation for the csv library.
    https://docs.python.org/3/library/csv.html#writer-objects

"""

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
# YOUR CODE HERE!
