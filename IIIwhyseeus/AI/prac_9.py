from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder # Import TransactionEncoder
import pandas as pd

# Sample transaction data (replace with your own)
transactions = [
    ['milk', 'bread', 'eggs'],
    ['milk', 'bread', 'beer'],
    ['milk', 'diaper', 'beer', 'eggs'],
    ['milk', 'bread', 'eggs', 'beer'],
    ['bread', 'beer', 'diaper']
]

# Create a pandas DataFrame from the transaction data
dataset = pd.DataFrame(transactions)
# One-hot encode the transaction data
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Apply Apriori algorithm to find frequent itemsets
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Generate association rules from frequent itemsets
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.6)

# Print the discovered rules
print(rules)