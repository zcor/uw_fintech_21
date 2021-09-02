# Create variables
company_name = "Frankfurter Finance"
years_in_business = 23
hourly_wage = 65.40
expert_status = True

# Print the variables
print(company_name)
print(years_in_business)
print(hourly_wage)
print(expert_status)

# Prints the data type of each declared variable
print("The data type of variable title is", type(company_name))
print("The data type of variable years is", type(years_in_business))
print("The data type of variable hourly_wage is", type(hourly_wage))
print("The data type of variable expert_status is", type(expert_status))

# Using variable names in calculations
total_miles = 257
gallons_gas = 7.2
miles_per_gallon = total_miles / gallons_gas

# Updating variables using assignment
miles = 48
kilometers = 0.621371 * miles

# Substituting/formatting variable
message = f"The total kilometers driven was: {kilometers}"
print(message)

# Two number values will be added
transaction_1 = 11.75
transaction_2 = 14.99

total_transaction_cost = transaction_1 + transaction_2
print(total_transaction_cost)

# Two string values will be concatenated
first_name = "Michelle"
last_name = "Jones"

full_name = first_name + last_name
print(full_name)
print("My name is " + first_name + " " + last_name + ".")

# Variable naming conventions
# Bad Example
mpg = 24

# Better Example
miles_per_gallon = 24
