import pandas as pd

df = pd.read_csv('air4thai_08t_2023-09-01_2024-02-27.csv')

print("Initial Data:")
print(df)

df.dropna(inplace=True, axis=1, thresh=5)

df.fillna(df.mean(axis=1), inplace=True)

df.to_csv('cleaned_air4thai.csv', index=False)

print("\nCleaned Data:")
print(df)
