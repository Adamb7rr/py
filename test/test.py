import pandas as pd

# data = {
#     'Name': ['Adam', 'Youseef', 'Ziad', 'Sabah'],
#     'Age': [23, 13, 20, 50],
#     'Location': ['New York', 'Chicago', 'United State', 'Cairo']
# }

df = pd.read_csv('people-100.csv')
# print(df.head())
print(df[['First Name', 'Job Title']])