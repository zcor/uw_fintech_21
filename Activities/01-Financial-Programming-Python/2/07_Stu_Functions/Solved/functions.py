# Calculating the cost of a new car

# Use the following future value formula from the dicts.py activity as reference
# future_value = current_loan_value * (1 + (annual_interest_rate)) ** months_remaining


# Create a function call calculate_future_value.
# The function should take in 3 arguments, the current_loan_value, the annual_interest_rate and the months_remaining.
# The function body should contain the future_value formula.
# The function should return the future_value.

def calculate_future_value(current_loan_value, annual_interest_rate, months_remaining):
    future_value = current_loan_value * (1 + (annual_interest_rate / 12)) ** months_remaining
    print("fv", future_value)
    return future_value


# Call the calculate_future_value function, passing the relevant information from the new_car_loan dictionary as parameters.
# Be sure to set the function call equal to a variable called cost_of_new_car. # Print the cost_of_new_car. Be sure to round the figure to 2 decimal places.

new_car_loan = {
    "current_loan_value": 25000,
    "months_remaining": 6,
    "annual_interest_rate": 0.085
}

cost_of_new_car = calculate_future_value(new_car_loan["current_loan_value"], new_car_loan["annual_interest_rate"], new_car_loan["months_remaining"])

print(f"The cost of the new car is ${cost_of_new_car: .2f}.")
