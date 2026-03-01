import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

data = pd.read_csv(r"F:\py\Data_analysis\NBA_project\all_seasons.csv")

print(data['player_height'].max())
print(data['player_height'].min())