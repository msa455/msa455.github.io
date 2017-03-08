import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import os
import random

Location = r'C:\Users\Main Character\Desktop\jeopardy\JEOPARDY_CSV.csv'

df = pd.read_csv(Location, names = ['Show Number', 'Air Date', 'Round',
                                    'Category', 'Value', 'Question', 'Answer'])

print(df.head())

UniqueCategories = df["Category"].unique()
print(UniqueCategories[:10])
