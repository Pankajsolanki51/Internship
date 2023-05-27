import pandas as pd
import matplotlib.pyplot as plt

file_names = [
    "flipkart_mobile_under_50000_10may23.csv",
    "flipkart_mobile_under_50000_11may23.csv",
    "flipkart_mobile_under_50000_15may23.csv",
    "flipkart_mobile_under_50000_16may23.csv",
    "flipkart_mobile_under_50000_17may23.csv",
    "flipkart_mobile_under_50000_18may23.csv"
]

data_frames = []
for file_name in file_names:
    df = pd.read_csv(file_name)
    data_frames.append(df)

# Concatenate all data frames into a single DataFrame
combined_df = pd.concat(data_frames, ignore_index=True)

# Assuming the columns are 0-indexed
brand_column = 1 # Update with the correct index for the column containing brand names

# Extract the brand names
brand_names = combined_df.iloc[:, brand_column]

# Count the occurrences of each phone brand
brand_counts = brand_names.value_counts()

# Define the phone brands of interest
brands_of_interest = ['Samsung', 'Apple', 'Realme', 'OnePlus', 'Google']

# Filter the brand counts for the brands of interest
filtered_counts = brand_counts[brand_counts.index.isin(brands_of_interest)]

# Create a pie plot
plt.pie(filtered_counts, labels=filtered_counts.index, autopct='%1.1f%%')

plt.title("Phone Brand Distribution")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

# Display the pie plot
plt.show()
