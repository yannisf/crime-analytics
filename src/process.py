import numpy as numpy
import pandas as pd

columns = ['code', 'theft', 'burglary', 'automotive', 'robbery', 'year',
'executed', 'attempts', 'solved', 'native_perpertrators', 'foreign_perpetrators']
df = pd.read_csv('../data/data.csv', names = columns)
df.fillna(0, inplace=True)
df.astype(int)

print(df.head())
