# Working with Dictionaries

# Following is a Python Dictionary containing student loan information.
# Notice all keys are defined as strings, but the values are declared in a variety of data types.

student_loan_information_aj = {
    "student_name": "Amy Johnson",
    "university": "Yale",
    "academic_year": "2015_2016",
    "loan_amount": 45000,
    "duration_years": 10,
    "payments_started": False,
}

# Using the student_loan_information_aj dictionary provided, complete the following actions:

# Print the original 'student_loan_information_aj' dictionary
print("The original student loan profile", student_loan_information_aj)

# Our student's name was spelled incorrectly.
# Update the value of the `student_name' key to `Amy Johnston`.
# Be sure to print the dictionary so that you know your changes are working.
student_loan_information_aj["student_name"] = "Amy Johnston"
print("The amended student loan profile:", student_loan_information_aj)


# Every loan should have an interest rate associated with its information.
# Add a key called 'interest_rate' and assign it a value of 3.5 percent (or 0.035).
# Print the dictionary so that you know your changes are working.
student_loan_information_aj["interest_rate"] = 0.035
print("The amended student loan profile:", student_loan_information_aj)


# Reviewing the information, it appears that the key for 'loan_amount' has been spelled incorrectly.
# You will need to delete the existing key:value pair and add one with the correct spelling.
# You can use the same amount of 45000.
# Print the dictionary so that you know your changes are working.
del student_loan_information_aj["loan_amount"]
student_loan_information_aj["loan_amount"] = 45000
print(f"The amended student loan profile: {student_loan_information_aj}")
