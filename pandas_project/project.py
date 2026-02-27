import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_excel("pandas_project/files/ecommerce_orders.xlsx")

# res = data['Product']
data.columns = data.columns.str.strip()
print(data['Product'])