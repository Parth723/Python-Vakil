import pandas as pd
import re

input_csv = 'user_data.csv'
output_csv = 'cleaned_user_data.csv'

def is_valid_email(email):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email) is not None

df = pd.read_csv(input_csv)

df_cleaned = df.drop_duplicates(subset='user_id')

df_cleaned = df_cleaned[df_cleaned['email'].apply(is_valid_email)] 

df_cleaned.to_csv(output_csv, index=False)

print(f'Cleaned data has been written to {output_csv}')
