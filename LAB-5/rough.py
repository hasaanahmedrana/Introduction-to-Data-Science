import pandas as pd
import numpy as np

# Load the Iris dataset (assuming it is in a CSV file named 'iris.csv')
iris = pd.read_csv('iris.csv')

# Task 1: Data Inspection and Missing Value Handling
# Inspect the dataset
missing_values = iris.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Handle missing values in numeric columns
numeric_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
for col in numeric_columns:
    iris[col].fillna(iris[col].mean(), inplace=True)

# Handle missing values in the categorical column
iris['species'].fillna(iris['species'].mode()[0], inplace=True)

# Task 2: Data Cleaning and Transformation
# Remove duplicate entries
iris.drop_duplicates(inplace=True)

# Create a new column for petal area
iris['petal_area'] = iris['petal_length'] * iris['petal_width']

# Drop rows with any remaining missing values
iris.dropna(inplace=True)

# Task 3: Aggregation and Transformation
# Convert species column to numeric
iris['species_numeric'] = iris['species'].astype('category').cat.codes

# Aggregation: Calculate mean of numeric columns grouped by species
aggregation = iris.groupby('species')[numeric_columns].mean()
print("Mean of numeric columns grouped by species:")
print(aggregation)

# Task 4: Advanced Reshaping
# Reshape the dataset to a long format
long_format = iris.melt(
    id_vars=['species', 'species_numeric'],
    value_vars=numeric_columns,
    var_name='measurement_type',
    value_name='measurement_value'
)
print("Long format of the dataset:")
print(long_format.head())

# Save the cleaned and reshaped datasets
iris.to_csv('cleaned_iris.csv', index=False)
long_format.to_csv('long_format_iris.csv', index=False)

print("Data cleaning, transformation, and reshaping completed.")
