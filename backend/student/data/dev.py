import pandas as pd


file_path = 'courses.csv'
output_path = 'courses_no_id.csv'

df = pd.read_csv(file_path)
df.drop('id', axis=1, inplace=True)

df.to_csv(output_path, index=False)
