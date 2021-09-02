# Starting to Function

In this activity, you'll practice working with Python functions.

## Background

Ever since you figured out how to calculate the total cost of the loan for your new car, all of your friends have been asking you to do their calculations.

It makes sense to put the future calculation in a function; this way, you only have to write the function once and then call it over and over.

Use the instructions and the starter file to create a `calculate_future_value` function and call it using the following `new_car_loan` dictionary:

```python
new_car_loan = {
    "current_loan_value" : 25000,
    "months_remaining" : 6,
    "annual_interest_rate" : 0.085,
    "repayment_interval" : "bullet"
}
```

## Instructions

Open the [starter file](Unsolved/functions.py) and complete the following steps.

1. Use the following future value formula for reference:

    ```python
    future_value = current_loan_value * (1 + (annual_interest_rate)) ** months_remaining
    ```

2. Create a function called `calculate_future_value` that fulfills the following criteria.

    * The function should take in three arguments: `current_loan_value`, `annual_interest_rate`, and `months_remaining`.

    * The function body should contain the `future_value` formula.

    * The function should return the `future_value`.

3. Call the `calculate_future_value` function, passing the relevant information from the `new_car_loan` dictionary as parameters. Make sure to set the function call equal to a variable called `cost_of_new_car`.

4. Print the `cost_of_new_car`. Round the figure to two decimal places.

---

© 2020 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
