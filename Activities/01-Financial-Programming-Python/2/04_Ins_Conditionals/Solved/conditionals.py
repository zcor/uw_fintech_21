# Demonstrate conditional statement

# if True:
#   Do something
# else:
#   Do something else

# Driverless car scenario
driverless_car = False

if True:
    # Do something
    print("Oh no! The driver's asleep! What do we do?!")
    print()
    print("All is good. Auto-pilot initiated.")
else:
    # Do something else
    print("Oh no! The driver's asleep! MAYDAY! MAYDAY!")

# Demonstrate conditional with print statement
is_raining = True

if is_raining:
    print("Bring an umbrella!")
else:
    print("Leave the umbrella at home!")


# Variable values can be established using conditional statements.
pedestrian = False

if not pedestrian:
    immediate_action = "drive"
else:
    immediate_action = "stop"


# Conditionals can be use to evaluate equality
x = 1
if x == 1:
    print("x is equal to 1")

y = 5
if y == 1:
    print("x is equal to 1")

# Or inequality
z = 9
if z != 1:
    print("y is not equal to 1")

# Declare variables and values for evaluation
x = 1
y = 10

# Multiple conditional can be utilized
if x == 1 and y == 10:
    print("Both values returned True")


# Nested if statements
if x < 10:
    if y < 5:
        print("x is less than 10 and y is less than 5")
    elif y == 5:
        print("x is less than 10 and y is equal to 5")
    else:
        print("x is less than 10 and y is greater than 5")

# Nested if statements with insurance premium predictor
accident = True
at_fault = False
accident_forgiveness = True
elite_status = True

increase_insurance_premium = True

print("Insurance premium will increase. True or False?")

# Nested Conditional Statements
if accident:
    if at_fault and accident_forgiveness:
        increase_insurance_premium = False
    elif at_fault and not accident_forgiveness and not elite_status:
        increase_insurance_premium = True
    else:
        increase_insurance_premium = False
elif not accident and elite_status:
    increase_insurance_premium = False
else:
    increase_insurance_premium = True

print(f"Prediction: {increase_insurance_premium}")
