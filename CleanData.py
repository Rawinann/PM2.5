import pandas as pd

df = pd.read_csv('air4thai_44t_2023-09-01_2024-02-27.csv')

print("Initial Data:")
print(df)

# Drop columns with fewer than 1 non-NaN value
df.dropna(inplace=True, axis=1, thresh=1)

# Convert non-numeric columns to numeric, excluding 'DATETIMEDATA' and 'stationID'
non_numeric_columns = ['DATETIMEDATA', 'stationID']
numeric_columns = [col for col in df.columns if col not in non_numeric_columns]
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Fill NaN values with the mean of each numeric column
df[numeric_columns] = df[numeric_columns].apply(lambda x: x.fillna(x.mean()))

# Save the cleaned data to a new CSV file
df.to_csv('cleaned_air4thai.csv', index=False)

print("\nCleaned Data:")
print(df)

