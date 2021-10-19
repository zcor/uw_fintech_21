# Segmenting Customers

Your marketing department has just come back to you regarding the initial analysis you performed on the customer ratings for mobile application and an in-person banker services. Although your initial analysis of grouping the customers into two segments was helpful, they are wondering if the data could be even more finely clustered.

You have been asked to review how the customer ratings data looks when modeled with 3 and 4 clusters.

Using the information contained in the [starter file](Unsolved/segmenting_customers.ipynb), apply the K-means algorithm to the `service_ratings` data using both 3 and 4 clusters to segment the customer information.

## Instruction

1. Review the Pandas DataFrame and plot associated with the import of the "service_ratings.csv" file.

2. Run the K-means algorithm identifying 3 clusters in the data.

    * Create and initialize the K-means model for 3 clusters . Use a `random_state` value of 1 for the model.
    * Fit, or train, the model using the `service_ratings_df` DataFrame
    * Make predictions about the clustering using the trained model. Save the predictions to a variable called `customer_segment_3`, and print that variable.
    * Add a column called "customer_segment_3", and add the `customer_segment_3` information to the column.
    * Plot the data using the DataFrame adjusted to include customer segment information for 3 clusters.

3. Run the K-means algorithm identifying 4 clusters in the data.

    * Create and initialize the K-means model for 4 clusters . Use a `random_state` value of 1 for the model.
    * Fit, or train, the model using the `service_ratings_df` DataFrame
    * Make predictions about the clustering using the trained model. Save the predictions to a variable called `customer_segment_4`, and print that variable.
    * Add a column called "customer_segment_4", and add the `customer_segment_4` information to the column.
    * Plot the data using the DataFrame adjusted to include customer segment information for 4 clusters.

4. Answer the following question: Can any additional information be gleaned from the customer segmentation data when clusters of 3 and 4 are applied?

---

© 2021 Trilogy Education Services, a 2U, Inc. brand. All Rights Reserved.
