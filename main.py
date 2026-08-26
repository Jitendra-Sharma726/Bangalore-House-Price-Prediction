import pandas as pd
import numpy as np

def convert_sqft_to_num(x):
    """
    This function converts the 'total_sqft' column to a numeric format.
    It handles ranges by taking their average.
    """
    # Split the string by '-'
    tokens = [] # Your code here

    # Check if the split resulted in two parts (a range)
    if False: # Your code here
        # If it's a range, calculate the average and return it.
        return 0.0 # Your code here
    
    # Use a try-except block to handle regular numbers and other cases.
    try:
        # Try converting the input to a float.
        return 0.0 # Your code here
    except:
        # If conversion fails, return None.
        return None


# --- Main execution block ---
if __name__ == "__main__":
    # 1. Load the dataset 'Bengaluru_House_Data.csv' into a pandas DataFrame.
    # Use a try-except block for robust file handling.
    try:
        df = None # Your code here
    except FileNotFoundError:
        print("Error: 'Bengaluru_House_Data.csv' not found. Please make sure it's in the same directory.")
        exit()


    # 2. Drop the columns 'area_type', 'society', 'balcony', and 'availability'.
    df_cleaned = df # Your code here
    
    # 3. Drop rows with any missing values.
    # df_cleaned = ... # Your code here

    # 4. Create the 'bhk' column from the 'size' column.
    # Hint: Use the .apply() method with a lambda function to split the string and get the first element.
    # df_cleaned['bhk'] = ... # Your code here

    # 5. Apply the 'convert_sqft_to_num' function to the 'total_sqft' column.
    # df_cleaned['total_sqft'] = ... # Your code here
    
    # Display the DataFrame info to see the changes
    print("--- Data types before final cleaning ---")
    # df_cleaned.info() # <-- Uncomment this line

    # 6. Drop any remaining rows with null values after the transformations.
    # df_cleaned = ... # Your code here
    
    print("\n--- Data types after final cleaning ---")
    # df_cleaned.info() # <-- Uncomment this line

    # 7. Save the cleaned DataFrame to 'cleaned_bengaluru_house_data.csv'.
    # Remember to set index=False.
    pass # Your code here
    
    print("\nCleaned data has been successfully saved to 'cleaned_bengaluru_house_data.csv'")
    print("\n--- First 5 rows of cleaned data ---")
    # print(df_cleaned.head()) # <-- Uncomment this line
