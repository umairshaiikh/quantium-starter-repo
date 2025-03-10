import pandas as pd

# Define the file paths
file_paths = [
    'daily_sales_data_0.csv',
    'daily_sales_data_1.csv',
    'daily_sales_data_2.csv'
]

# Print the file paths to verify
print("File paths:", file_paths)

# Load the CSV files into dataframes
dataframes = []
for file in file_paths:
    try:
        df = pd.read_csv(file)
        dataframes.append(df)
        print(f"Successfully loaded {file}")
    except FileNotFoundError:
        print(f"Error: {file} not found")

# Initialize an empty list to store the processed data
processed_data = []

# Loop through each dataframe
for df in dataframes:
    # Filter rows where the product is 'Pink Morsel'
    pink_morsel_df = df[df['product'] == 'Pink Morsel']
    
    # Calculate sales by multiplying quantity and price
    pink_morsel_df['sales'] = pink_morsel_df['quantity'] * pink_morsel_df['price']
    
    # Select only the required columns
    selected_columns = ['sales', 'date', 'region']
    processed_df = pink_morsel_df[selected_columns]
    
    # Append the processed dataframe to the list
    processed_data.append(processed_df)

# Concatenate all processed dataframes into a single dataframe
combined_df = pd.concat(processed_data, ignore_index=True)

# Define the output file path
output_file_path = 'processed_sales_data.csv'

# Save the combined dataframe to a new CSV file
combined_df.to_csv(output_file_path, index=False)
print(f"Processed data saved to {output_file_path}")
