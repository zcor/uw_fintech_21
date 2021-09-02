# Loop-De_Loop - Solution

# Looping through a List

# List of Portfolio gains and losses for the investment period of February, 2019.
portfolio_gain_loss_list = [
    168.48, 2445.21, 1461.00, -461.98,
    -3368.62, 427.03, 193.99, 4443.63,
    1132.76, -779.18, 3372.93, 604.64,
    703.99, -1249.01, 2156.62, 475.81,
    -250.61, -150.43, -653.08
]


# Using a for loop calculate the total sum of gains and losses for the period. Print the result rounded to 2 decimal places.

sum_list = 0.00

for day in portfolio_gain_loss_list:
    sum_list += day

print("Total gain_loss", round(sum_list, 2))

# Using the len() method determine the number of days in the investment period. Set that value equal to a variable called `number_of_days`. Print the value.

number_of_days = len(portfolio_gain_loss_list)
print("The number of days in the period was", number_of_days)

# Use the sum_list and number_of_days variables to determine the `average_gain_loss_per_day` value. Print that value, rounding it to 2 decimal places.

average_gain_loss_per_day = sum_list / number_of_days

print("The average gain/loss per day was", round(average_gain_loss_per_day, 2))


# Looping through a dictionary

# Dictionary of portfolio gains and losses for the investment period of February, 2019.
portfolio_gain_loss_dict = {
    "02-01-2019": 168.48,
    "02_04-2019": 2445.21,
    "02-05-2019": 1461.00,
    "02-06-2019": -461.98,
    "02-07-2019": -3368.62,
    "02-08-2019": 427.03,
    "02-11-2019": 193.99,
    "02-12-2019": 4443.63,
    "02-13-2019": 1132.76,
    "02-14-2019": -779.18,
    "02-15-2019": 3372.93,
    "02-19-2019": 604.64,
    "02-20-2019": 703.99,
    "02-21-2019": -1249.01,
    "02-22-2019": 2156.62,
    "02-25-2019": 475.81,
    "02-26-2019": -250.61,
    "02-27-2019": -150.43,
    "02-28-2019": -653.08
}


# Using a for loop calculate the total sum of gains and losses for the period. Print the result rounded to 2 decimal places.
# Hint - This total should match the one calculated from looping through the list.

sum_dict = 0.00

for key in portfolio_gain_loss_dict:
    sum_dict += portfolio_gain_loss_dict[key]

print("Total gain_loss", round(sum_dict, 2))


#  Conditionally filter the dictionary to find the days with a gain greater than or equal to $1000, or a loss less than or equal to -$1000. Add these gain or loss VALUES only to the appropriate list. Print both lists.

big_gains = []
big_losses = []

for key in portfolio_gain_loss_dict:
    if portfolio_gain_loss_dict[key] >= 1000:
        big_gains.append(portfolio_gain_loss_dict[key])
    if portfolio_gain_loss_dict[key] <= -1000:
        big_losses.append(portfolio_gain_loss_dict[key])

print("The biggest gains were:", big_gains)
print("The biggest losses were:", big_losses)


# Loop through both lists to determine if the days with the big gains were more profitable than the days with the big losses

total_big_gains = 0.00
total_big_losses = 0.00

for gain in big_gains:
    total_big_gains += gain

for loss in big_losses:
    total_big_losses += loss

print("The big gains total was", round(total_big_gains, 2))
print("The big losses total was", round(total_big_losses, 2))
