# Association-rules
The file Groceries.csv contains market basket data. The variables are:
1.	Customer: Customer Identifier
2.	Item: Name of Product Purchased
After you have imported the CSV file, please discover association rules using this dataset.  For your information, the observations have been sorted in ascending order by Customer and then by Item.  Also, duplicated items for each customer have been removed.  
a)	Create a data frame that contains the number of unique items in each customer’s market basket. Draw a histogram of the number of unique items.  What are the 25th, 50th, and the 75th percentiles of the histogram?

b)	We are only interested in the k-itemsets that can be found in the market baskets of at least seventy five (75) customers.  How many itemsets can we find?  Also, what is the largest k value among our itemsets?

c)	Find out the association rules whose Confidence metrics are greater than or equal to 1%.  How many association rules can we find?  Please be reminded that a rule must have a non-empty antecedent and a non-empty consequent.  Please do not display those rules in your answer.

d)	Plot the Support metrics on the vertical axis against the Confidence metrics on the horizontal axis for the rules you have found in (c).  Please use the Lift metrics to indicate the size of the marker.
 
e)	List the rules whose Confidence metrics are greater than or equal to 60%.  Please include their Support and Lift metrics.
