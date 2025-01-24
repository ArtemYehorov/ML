import numpy as np
import pandas as pd

df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
ser1 = pd.Series([10, 20, 30, 40, 50])

df1.columns = ["A", "B", "C"]
ser1.index = ["a", "b", "c", "d", "e"]

ser1_max = ser1.max()

df2_mean = df1.median(axis=1)

ser1_sum = ser1.sum()

df2_filtered = df1[df1["A"] < 5]

df1["D"] = [10, 20, 30]

df1 = df1.drop(columns="B")

print(df1)

