# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oLGkOrbslg0XUXNEqSSaPmE8opHcL6bE
"""

from google.colab import files
import pandas as pd

# Upload the CSV file
uploaded = files.upload()

# Load the uploaded CSV file into a pandas DataFrame
# Replace 'filename.csv' with the actual file name after upload
df = pd.read_csv(list(uploaded.keys())[0])

# Display the first few rows to check if it's loaded correctly
df.head()

# Load your CSV file
df = pd.read_csv(list(uploaded.keys())[0])

# Clean the 'Price' column by removing the dollar sign and converting to float
data['Price'] = data['Price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

# Extract numeric rating from the 'Rating' column using regex
data['Rating'] = data['Rating'].str.extract(r'(\d\.\d)').astype(float)

# Display cleaned data
print(data[['Sub Category', 'Price', 'Rating']].head())

# Load your CSV file
df = pd.read_csv(list(uploaded.keys())[0])

# Clean the 'Price' column by removing the dollar sign and converting to float
df['Price'] = df['Price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

# Extract numeric rating from the 'Rating' column using regex
df['Rating'] = df['Rating'].str.extract(r'(\d\.\d)').astype(float)

# Display cleaned data
print(df[['Sub Category', 'Price', 'Rating']].head())

# Load your CSV file
df = pd.read_csv(list(uploaded.keys())[0])

# Clean the 'Price' column by removing the dollar sign and converting to float
df['Price'] = df['Price'].str.replace('$', '', regex=True) # Remove dollar signs
df['Price'] = df['Price'].str.replace(',', '', regex=True) # Remove commas
df['Price'] = df['Price'].str.split('through-', n=1, expand=True)[0] # Keep only the first price in a range


# Extract numeric rating from the 'Rating' column using regex
df['Rating'] = df['Rating'].str.extract(r'(\d\.\d)').astype(float)

# Display cleaned data
print(df[['Sub Category', 'Price', 'Rating']].head())

# Calculate average price and rating
average_price = data['Price'].mean()
average_rating = data['Rating'].mean()

print(f'Average Price: ${average_price:.2f}')
print(f'Average Rating: {average_rating:.2f}')

# Calculate average price and rating
average_price = df['Price'].mean() # Changed 'data' to 'df'
average_rating = df['Rating'].mean() # Changed 'data' to 'df'

print(f'Average Price: ${average_price:.2f}')
print(f'Average Rating: {average_rating:.2f}')

# Calculate average price and rating
average_price = pd.to_numeric(df['Price']).mean() # Converted 'Price' column to numeric using pd.to_numeric
average_rating = df['Rating'].mean()

print(f'Average Price: ${average_price:.2f}')
print(f'Average Rating: {average_rating:.2f}')

# Group by 'Sub Category' and calculate average price
avg_price_by_category = data.groupby('Sub Category')['Price'].mean()

# Plot the data
avg_price_by_category.plot(kind='bar', color='skyblue')
plt.title('Average Price by Sub Category')
plt.xlabel('Sub Category')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.show()

# Remove the dollar sign and commas from the 'Price' column and convert to float
df['Price'] = df['Price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

# Extract numeric rating from the 'Rating' column using regular expressions
df['Rating'] = df['Rating'].str.extract(r'(\d\.\d)').astype(float)

# Remove the dollar sign and commas from the 'Price' column and convert to float
df['Price'] = df['Price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

# Convert 'Rating' column to string type
df['Rating'] = df['Rating'].astype(str)

# Extract numeric rating from the 'Rating' column using regular expressions
df['Rating'] = df['Rating'].str.extract(r'(\d\.\d)').astype(float)

# Check for missing values
print(df.isnull().sum())

# Option 1: Drop rows with missing values
df = df.dropna()

# Option 2: Fill missing values (e.g., with median values for numerical columns)
df['Price'].fillna(df['Price'].median(), inplace=True)
df['Rating'].fillna(df['Rating'].mean(), inplace=True)

# Remove duplicate rows if any
df = df.drop_duplicates()

# Convert 'Date' column (if applicable) to datetime format
# df['Date'] = pd.to_datetime(df['Date'])

# Convert other columns to the appropriate types if needed
df['Price'] = df['Price'].astype(float)  # Ensure 'Price' is float

# Rename columns for better readability
df.rename(columns={'Sub Category': 'Sub_Category', 'Product Description': 'Product_Description'}, inplace=True)

# Drop columns that are not needed for analysis
df = df.drop(columns=['Currency', 'Feature', 'Product Description'])

# Drop columns that are not needed for analysis
df = df.drop(columns=['Currency', 'Feature', 'Product_Description']) # Changed 'Product Description' to 'Product_Description'

# Display the cleaned data
print(df.head())

# Calculate average price
average_price = df['Price'].mean()
print(f'Average Price: ${average_price:.2f}')

# Calculate average rating
average_rating = df['Rating'].mean()
print(f'Average Rating: {average_rating:.2f}')

# Most expensive product
most_expensive = df[df['Price'] == df['Price'].max()]
print(f'Most Expensive Product: {most_expensive["Title"].values[0]}')

# Products with the highest rating
top_rated = df[df['Rating'] == df['Rating'].max()]
print(f'Highest Rated Product: {top_rated["Title"].values[0]}')

import matplotlib.pyplot as plt

# Group by Sub_Category and calculate the average price
avg_price_by_category = df.groupby('Sub_Category')['Price'].mean()

# Plotting the bar chart
avg_price_by_category.plot(kind='bar', color='skyblue', figsize=(10,6))
plt.title('Average Price by Sub Category')
plt.xlabel('Sub Category')
plt.ylabel('Average Price')
plt.xticks(rotation=45)
plt.show()

# Plotting the histogram
plt.figure(figsize=(10,6))
plt.hist(df['Price'], bins=20, color='purple')
plt.title('Distribution of Product Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Scatter plot of Rating vs Price
plt.figure(figsize=(10,6))
plt.scatter(df['Price'], df['Rating'], alpha=0.5, color='green')
plt.title('Rating vs Price')
plt.xlabel('Price')
plt.ylabel('Rating')
plt.show()

# Pie chart for product distribution by sub-category
sub_category_counts = df['Sub_Category'].value_counts()

plt.figure(figsize=(8,8))
plt.pie(sub_category_counts, labels=sub_category_counts.index, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Distribution of Products by Sub Category')
plt.show()

