import pandas as pd
fpath = "Pandas_data1.csv"
ratings = pd.read_csv(fpath)
print('head()')
print(ratings.head())

print('shapes')
print(ratings.shape)

print('columns')
print(ratings.columns)

print('index')
print(ratings.index)

print('dtypes------------')
print(ratings.dtypes)