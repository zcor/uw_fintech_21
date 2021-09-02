# Loop De Loop

In this activity, you’ll explore a number of use cases for loops. This will help you gain more experience iterating through both lists and dictionaries.

## Background

You’re reviewing the performance of your portfolio during the month of February 2019. In this activity, you'll use loops to help determine the net total of gains and losses for the period. You will also use loops to determine the days that had big gains versus the days that had big losses.

## Instructions

Using the [starter code](Unsolved/loops.py) provided, loop through the provided list and dictionary to find the information specified by the instructions.

### Loop Through a List

Here is the list of portfolio gains and losses for the investment period of February 2019:

```python
portfolio_gain_loss_list = [
    168.48, 2445.21, 1461.00, -461.98,
    -3368.62, 427.03, 193.99, 4443.63,
    1132.76, -779.18, 3372.93, 604.64,
    703.99, -1249.01, 2156.62, 475.81,
    -250.61, -150.43, -653.08
]
```

1. Using a `for` loop, calculate the total sum of gains and losses for the period. Print the result.

2. Using the `len` function, determine the number of days in the investment period. Set that value equal to a variable called `number_of_days`. Print the value.

3. Use the `sum_list` and `number_of_days` variables to determine the `average_gain_loss_per_day` value.  Print that value, rounding it to two decimal places.

#### Looping Through a Dictionary

Here is the dictionary of portfolio gains and losses for the investment period of February 2019:

```python
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
```

1. Using a `for` loop, calculate the total sum of gains and losses for the period. Print the result.

    **Hint:** This total should match the one calculated from looping through the list.

2. Conditionally filter the dictionary to find the days with a gain greater than or equal to $1,000, or a loss of less than or equal to -$1,000. Add these gain or loss values only to either the `big_gains` list or `big_losses` list. Print both lists.

3. Loop through both the `big_gains` and `big_losses` lists to determine whether the days with the big gains were more profitable than the days with the big losses were painful.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
