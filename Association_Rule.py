'''
Name: Olugbenga Abdulai
CWID: A20447331
'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

'''
Q1(a)
'''
# reading the data
groceries = pd.read_csv(r"C:\Users\abdul\Desktop\CS 584\HW\HW 2\Groceries.csv")

# getting unique items
unique_items = groceries.groupby('Customer').Item.count()
print("Unique Items count:\n", unique_items)

# histogram plot
sns.distplot(unique_items, kde=False, color='blue', hist_kws={'edgecolor':'black'})
plt.title("Histogram of unique item count")
plt.show()

# getting the quantiles
first_quart, med, third_quart = np.percentile(unique_items, [25, 50, 75])
print("\nfirst quartile: ", first_quart)
print("second quartile: ", med)
print("third quartile: ", third_quart)

'''
Q1(b)
'''
# converting the groceries data to a list format for transaction encoder
list_item = groceries.groupby(['Customer'])['Item'].apply(list).values.tolist()

# encoding list_item
t_enc = TransactionEncoder()
encoded = t_enc.fit_transform(list_item)

# converting the encoded values to a dataframe
item_indicator = pd.DataFrame(encoded, columns=t_enc.columns_)
print("\nItem indicator:\n", item_indicator)

# Obtaining the minimum support value
num_customers = len(unique_items)
support = 75 / num_customers
print("\nsupport required: ", support)

# obtaining the frequent item sets
freq_itemsets = apriori(item_indicator, min_support=support, use_colnames=True)
print("\nfrequent item sets:\n", freq_itemsets.sort_values('support', ascending=False))

# obtaining the number of item sets
print("\nNumber of item sets: ", freq_itemsets.shape[0])

# obtaining largest k-value
vect = np.vectorize(len)
maxi = vect(freq_itemsets.itemsets.values).max(axis=0)
print("\nlargest k value: ", maxi)

'''
Q1(c)
'''
# obtaining association rules and count
assoc_rules = association_rules(freq_itemsets, metric="confidence", min_threshold=0.01)
print("\nAssociation rules with 1% threshold:\n", assoc_rules.head(10))
print("\nNumber of association rules: ", assoc_rules.shape[0])

'''
Q1(d)
'''
# scatter plot of support against lift
sns.scatterplot(assoc_rules.confidence, assoc_rules.support, size=assoc_rules.lift)
plt.title("Scatter plot of support versus lift")
plt.show()

'''
Q1(e)
'''
# obtaining high confidence rules
high_confid = assoc_rules[assoc_rules['confidence'] >= 0.6]
print("\nhigh confidence rules:\n", high_confid[['confidence', 'support', 'lift']])

