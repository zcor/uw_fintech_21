
######################
# Create Character One
######################

# Make a variable called `c1_name` and have it equal a string of "Mr. Farley".
c1_name = "Mr. Farley"

# Make a variable called `c1_age` and have it equal to an integer of 65.
c1_age = 65

# Make a variable called `c1_location` and have it equal to "San Francisco, CA".
c1_location = "San Francisco, CA"

# Make a variable called `c1_profession` and have it equal to "Web Developer".
c1_profession = "Web Developer"


######################
# Create Character Two
######################

# Make a variable called `c2_name` and have it equal a string of "Mr. Snuggles".
c2_name = "Mr. Snuggles"

# Make a variable called `c2_age` and have it equal to an integer of 30.
c2_age = 30

# Make a variable called `c2_location` and have it equal to "Oakland, CA".
c2_location = "Oakland, CA"

# Make a variable called `c2_profession` and have it equal "Accountant"
c2_profession = "Accountant"


##############
# Conditionals
##############

# Write an if-else statement to check if `c1_name` is equal to "Mr. Farley".
# If so, print a string of "Hello Mr. Farley" using the `c1_name` variable.
# If not, print a string of "Hello stranger".
if c1_name == "Mr. Farley":
    print(f"Hello {c1_name}")
else:
    print("Hello stranger!")


# Write an if-else statement to check if `c2_age` is greater than `c1_age`.
# If so, print a string of "Mr. Farley is older than Mr. Snuggles".
# Else if `c1_age` is greater than `c2_age`, print a string of "Mr. Snuggles is older than Mr. Farley".
# Else, `c1_age` must have to be equal to `c2_age`, therefore print a string of "Mr. Farley is the same age as Mr. Snuggles".
if c2_age > c1_age:
    print("Mr. Farley is older than Mr. Snuggles")
elif c1_age > c2_age:
    print("Mr. Snuggles is older than Mr. Farley")
else:
    print("Mr. Farley is the same age as Mr. Snuggles")


# Write an if-else statement to check if `c1_profession` is equal to "Web Developer" AND `c2_profession` is equal to "Accountant".
# If so, print a string of "Look a Web Developer and an Accountant".
# Else, print a string of "They are professionals."
if c1_profession == "Web Developer" and c2_profession == "Accountant":
    print("Look a Web Developer and an Accountant")
else:
    print("They are professionals")


# Write an if-else statement to check if `c1_location` is equal to "Oakland, CA".
# If so, print a string of "Mr. Farley comes from the home of the Raiders!".
# Else if `c2_location` is equal to a string of "San Francisco, CA", print a string of "Mr. Farley comes from the home of the 49ers!".
# Else, both conditions must not apply and therefore print a string "Mr. Farley doesn't hail from a sports town."
if c1_location == "Oakland, CA":
    print("Mr. Farley comes from the home of the Raiders!")
elif c2_location == "San Francisco, CA":
    print("Mr. Farley comes from the home of the 49ers!")
else:
    print("Mr. Farley doesn't hail from a sports town.")
