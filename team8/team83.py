import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Number of samples
num_samples = 1000

# Generate random data
age = np.random.randint(18, 70, size=num_samples)
gender = np.random.choice(['Male', 'Female'], size=num_samples)
annual_income = np.random.randint(20000, 150000, size=num_samples)
browsing_time = np.random.uniform(1, 30, size=num_samples)  # in minutes
items_in_cart = np.random.randint(0, 20, size=num_samples)
purchase = np.random.choice([0, 1], size=num_samples)  # 1 for purchase, 0 for no purchase

# Create a DataFrame
data = pd.DataFrame({
    'Age': age,
    'Gender': gender,
    'Annual_Income': annual_income,
    'Browsing_Time': browsing_time,
    'Items_in_Cart': items_in_cart,
    'Purchase': purchase
})

# Save the dataset to a CSV file
data.to_csv('ecommerce_data.csv', index=False)

print("Dataset created and saved as 'ecommerce_data.csv'")
