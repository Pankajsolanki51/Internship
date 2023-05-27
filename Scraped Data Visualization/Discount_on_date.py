import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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
product_column = 1  # Update with the correct index for the column containing product names
discount_column = 7  # Update with the correct index for the column containing discounts
date_column = 8  # Update with the correct index for the column containing dates

# Extract the relevant columns for analysis
product_discounts = combined_df.iloc[:, [product_column, discount_column, date_column]]

# Remove '%' and ' off' from discount values and convert to float
product_discounts["Discount"] = product_discounts["Discount"].str.replace('%', '').str.replace(' off', '').astype(float)

# Group the data by product, and find the maximum discount and corresponding date
grouped_data = product_discounts.groupby("Product Name").agg({"Discount": "max", "Date": "first"}).reset_index()

# Sort the data by the maximum discount in descending order
sorted_data = grouped_data.sort_values("Discount", ascending=False)

# Create a color map with a unique color for each product
num_products = len(sorted_data)
color_map = plt.get_cmap("tab10")
colors = color_map(np.linspace(0, 1, num_products))

# Plot the graph with the date and highest discount for each product
for i, row in sorted_data.iterrows():
    plt.bar(row["Date"], row["Discount"], color=colors[i], label=row["Product Name"])
    plt.text(row["Date"], row["Discount"], f"{row['Discount']}%", ha='center', va='bottom')

plt.xlabel("Date")
plt.ylabel("Discount (%)")
plt.title("Highest Discount Comparison")
plt.xticks(rotation=45)

# Add the legend with different colors for each product
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Display the graph
plt.show()
