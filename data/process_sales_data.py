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
        print(df.head())  # Print the first few rows of the dataframe
        print(df.info())  # Print information about the dataframe
    except FileNotFoundError:
        print(f"Error: {file} not found")

# Initialize an empty list to store the processed data
processed_data = []

# Loop through each dataframe
for df in dataframes:
    # Convert product column to title case for consistent matching
    df['product'] = df['product'].str.title()
    
    # Filter rows where the product is 'Pink Morsel'
    pink_morsel_df = df[df['product'] == 'Pink Morsel']
    print(f"Filtered 'Pink Morsel' from {len(df)} rows to {len(pink_morsel_df)} rows")
    
    if len(pink_morsel_df) == 0:
        print(f"No 'Pink Morsel' rows found in {file}")
    else:
        # Calculate sales by multiplying quantity and price
        pink_morsel_df['sales'] = pink_morsel_df['quantity'] * pink_morsel_df['price'].str.replace('$', '').astype(float)
        
        # Select only the required columns
        selected_columns = ['sales', 'date', 'region']
        processed_df = pink_morsel_df[selected_columns]
        print(f"Processed dataframe:\n{processed_df.head()}")
        
        # Append the processed dataframe to the list
        processed_data.append(processed_df)

# Concatenate all processed dataframes into a single dataframe
if processed_data:
    combined_df = pd.concat(processed_data, ignore_index=True)
    print(f"Combined dataframe:\n{combined_df.head()}")
else:
    print("No data to concatenate")

# Define the output file path
output_file_path = 'processed_sales_data.csv'

# Save the combined dataframe to a new CSV file
if processed_data:
    combined_df.to_csv(output_file_path, index=False)
    print(f"Processed data saved to {output_file_path}")
else:
    print("No data to save")
