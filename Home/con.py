import pandas as pd

# Load the Excel file (update the path to your actual Excel file)
excel_file_path = 'path_to_your_excel_file.xlsx'
df = pd.read_excel(r"C:\Users\shres\Desktop\PBL PROJECT\Home\data_viz1.csv")

# Check the data to make sure it’s loaded correctly (optional)
print(df.head())

# You can preprocess here if needed (e.g., handle missing values, encoding, etc.)
# For example, if the data has missing values:
df.fillna(0, inplace=True)  # Filling missing values with 0 (adjust as needed)

# Save the DataFrame as a pickle file
df.to_pickle('df.pkl')

print("df.pkl created successfully!")
