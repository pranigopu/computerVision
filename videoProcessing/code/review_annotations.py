# REVIEW ANNOTATIONS

import pandas as pd

#================================================
data = pd.read_csv('annotations.csv')
print('\nDATA REVIEW')
print('\nViewing a few rows...')
print(data.head(5))
print('\nViewing category counts...')
print(data['category'].value_counts())