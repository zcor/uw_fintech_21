# Variables

# This is a comment - any code commented out is not run -
# meaning that any code or text commented out is ignored.

"""
this is a multi-line comment
You can comment out many lines at once.
For the most part you will see single line comments
but it is good to see this.
As in single line comments, any code contained within multi-line comments are not run -
meaning that any code commented out is ignored.
"""

# Topic: Strings

# Create a variable named `subject` and assign a value of "Programmers to the variable `subject`.
subject = "Programmers"

# Create a variable, `first_name`, and assign it a value of a string, "Ada".

first_name = "Ada"

# Create a variable, `last_name`, and assign it a value of a string, "Lovelace".
last_name = "Lovelace"

# Create a variable, `full_name`, and assign it a value of the combination of `first_name` and `last_name` with a space.
full_name = f"{first_name} {last_name}"

# Create a variable, `profession`, and assign it a value of a string, "Computer Programmer".
profession = "Computer Programmer"

# Create a variable, `first_algorithm`, and assign it a value of a string, "Analytical Engine".
first_algorithm = "Analytical Engine"

# Create a variable, `city_location`, and assign it a value of a string, "London".
city_location = "London"

# Create a variable, `country_location`, and assign it a value of a string, "England".
country_location = "England"


# Topic: Integers

# Create a variable, `birth_year`, and assign it with an integer of 1815.
birth_year = 1815

# Create a variable, death_year, and assign it with an integer of 1852.
death_year = 1852

# Create a variable, age_at_passing, and assign it a value of death_year minus birth_year.
age_at_passing = death_year - birth_year

nationality = "British"

known_for = "First Computer Programmer"

#Topic: Print

# Print: "First Name: " and `first_name`.
print(f"First Name: {first_name}")

# Print: "Last Name: " and `last_name`.
print(f"Last Name: {last_name}")

# Print: "Profession: " and `profession`.
print(f"Profession: {profession}")

# Print: "BirthYear: " and `birth_year`.
print(f"Birth Year: {birth_year}")


# Topic: Concat Values

# Create and print a variable, `statement_one`, by assigning it a value of a string:
# "Programmers: Ada Lovelace is a British Computer Programmer born in 1815."
statement_one = f"{subject}: {first_name} {last_name} is a {nationality} {profession} born in {birth_year}."
print(statement_one)

# Create and print a variable, `statement_two`, by assigning it a value of a string:
# "She is commonly referred to as the First Computer Programmer."
statement_two = f"She is commonly referred to as a {known_for}."
print(statement_two)


# Create and print a variable, `statement_four`, by assigning it a value of a string:
# "She was a British Citizen who lived in London, England until her passing in 1852 at the age of 37."
statement_four = f"She was a {nationality} Citizen who lived in {city_location}, {country_location} until her passing in {death_year} at the age of {age_at_passing}."
print(statement_four)
