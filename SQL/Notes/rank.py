import pandas as pd

data = {'Score': [78, 85, 85, 86, 90, 96]}
df = pd.DataFrame(data)

# Default ranking (average method, ascending)
df['Rank_Average'] = df['Score'].rank()

# Ranking with 'dense' method
df['Rank_Dense'] = df['Score'].rank(method='dense')

# Ranking with 'min' method
df['Rank_Min'] = df['Score'].rank(method='min')

# Ranking with 'max' method
df['Rank_Max'] = df['Score'].rank(method='max')

# Ranking with 'first' method
df['Rank_First'] = df['Score'].rank(method='first')

# Ranking in descending order
df['Rank_Descending'] = df['Score'].rank(ascending=False)

print(df)