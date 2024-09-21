import pandas as pd
import random
import faker

fake = faker.Faker()

def generate_mock_data(num_entries):
    data = []
    for _ in range(num_entries):
        user_id = random.randint(1, 1000) 
        username = fake.user_name()
        email = fake.email() if random.choice([True, False]) else fake.word() 
        data.append([user_id, username, email])
    return data

num_entries = 100

columns = ['user_id', 'username', 'email']
mock_data = generate_mock_data(num_entries)
df = pd.DataFrame(mock_data, columns=columns)

input_csv = 'user_data.csv'
df.to_csv(input_csv, index=False)

print(f'Mock data has been written to {input_csv}')
