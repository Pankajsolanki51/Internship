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
product_column = 1  # Product Name
price_column = 2  # Prices
date_column = 8  # Date

# Remove rows with missing values
combined_df = combined_df.dropna(subset=["Prices"])

# Convert the "Prices" column to numeric
combined_df["Prices"] = combined_df["Prices"].replace('[\₹,]', '', regex=True).astype(float)

# Group the data by date and find the product with the minimum price
cheapest_products = combined_df.groupby("Date").apply(lambda x: x.loc[x["Prices"].idxmin()])

# Create a color map with a unique color for each product
num_products = len(cheapest_products)
color_map = plt.get_cmap("tab10")
colors = color_map(range(num_products))

# Plot the graph
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed
for i, (_, row) in enumerate(cheapest_products.iterrows()):
    plt.bar(row["Date"], row["Prices"], color=colors[i], label=row["Product Name"])

    # Add price labels above the bars
    plt.text(row["Date"], row["Prices"] + 10, f"₹{row['Prices']}", ha='center', va='bottom')

plt.xlabel("Date")
plt.ylabel("Price (in ₹)")
plt.title("Cheapest Product Comparison")
plt.xticks(rotation=45)
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

# Display the graph
plt.tight_layout()
plt.show()
