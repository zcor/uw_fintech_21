# Finding k

You have been analyzing the pricing data on one of the stocks your firm owns. Specifically, you were examining the relationship between the day's trading volume and the spread between the high and low trading price.

Using the information contained in the [starter file](Unsolved/finding_k.ipynb), use the elbow method to determine the optimal number of clusters, `k`, that should be used to segment these trades. Once the elbow curve has been established, evaluate the two most likely values for `k` using the K-means algorithm and a scatter plot.

## Instructions

1. Read in the `stock_data.csv` file from the Resources folder and create a DataFrame. Set the “date” column to create the DatetimeIndex. Be sure to include parameters for `parse_dates` and `infer_datetime_format`.

2. Create two lists: one to hold the list of inertia scores and another for the range of k values (from 1 to 11) to analyze.

3. Using a for-loop to evaluate each instance of k, define a K-means model, fit the K-means model based on the DataFrame, and append the model’s inertia to the empty inertia list that you created in Step 2.

4. Store the values for k and the inertia in a Dictionary called `elbow_data`. Use `elbow_data` to create a Pandas DataFrame called `df_elbow`.

5. Using hvPlot, plot the `df_elbow` DataFrame to visualize the elbow curve.

6. Perform the following tasks for each of the two most likely values of `k`:

    * Define a K-means model using `k` to define the clusters, fit the model, make predictions, and add the prediction values to the `spread_df` DataFrame.

    * Plot the clusters. The x-axis should reflect the "hi_low_spread", and the y-axis should reflect the "volume".

7. Answer the following question: Considering the plot, what’s the best number of clusters to choose, or value of k?

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
