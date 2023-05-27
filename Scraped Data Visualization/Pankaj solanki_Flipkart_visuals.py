# bar graph between product name and price of product
'''
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("flipkart_mobile_under_50000_17may23.csv")

# Extract the columns of interest
product_name = df['Product Name']
prices = df['Prices']

max_name_length = 15
display_name = [name[:max_name_length] + '...' if len(name) > max_name_length else name for name in product_name]
# Create the plot
plt.figure(figsize=(10, 8))
plt.bar(display_name, prices, color='hotpink')
plt.xticks(rotation=90)
plt.xlabel('Product Name', color='b', fontsize=15)
plt.ylabel('Prices', color='b',fontsize=15)
plt.title('Mobile Prices on Flipkart (17 May 2023)', color='red')

# Display the plot
plt.tight_layout()
plt.show()

'''
# plot between product name and ratings
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv("flipkart_mobile_under_50000_17may23.csv")

# Select the desired columns for the pie chart
product_names = df["Product Name"]
ratings = df["Rating"]

# Calculate the count of each rating
rating_counts = ratings.value_counts()

# Plot the pie chart
plt.figure(figsize=(8, 6))
explode = [0.1] * len(rating_counts)  # Create an explode array for slices
colors = plt.cm.Set2(range(len(rating_counts)))  # Set color scheme

# Filter out slices with less than 5% percentage
threshold_percentage = 10
filtered_counts = rating_counts[rating_counts > threshold_percentage]
filtered_labels = filtered_counts.index.tolist()
filtered_explode = [0.1] * len(filtered_labels)
filtered_colors = plt.cm.Set3(range(len(filtered_labels)))

patches, texts, autotexts = plt.pie(
    filtered_counts,
    labels=filtered_labels,
    explode=filtered_explode,
    colors=filtered_colors,
    autopct="%1.1f%%",
    startangle=90,
)

# Add legend and product names with colors
plt.legend(patches, product_names, loc="center right")
for text, color in zip(texts, colors):
    text.set_color(color)

plt.title("Flipkart Product v/s Product Ratings 17 may 2023 ")
plt.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle
plt.show()

'''
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a pandas DataFrame
data = pd.read_csv('flipkart_mobile_under_50000_17may23.csv')

# Extract the required columns
product_name = data['Product Name']
discounts = data['Discount']

# Create a list of colors for the stackplot
colors = ['purple', 'lightgreen', 'lightcoral', 'lightsalmon']
max_name_length = 15
display_name = [name[:max_name_length] + '...' if len(name) > max_name_length else name for name in product_name]
# Create the stackplot
plt.figure(figsize=(8, 6))
plt.stackplot(display_name, discounts, colors=colors)

# Customize the plot
plt.title('Mobile Discounts on Flipkart (17 May 23)')
plt.xlabel('Product Name',color='blue', fontsize=15)
plt.ylabel('Discount', color='blue',fontsize=15)
plt.xticks(rotation=90)
plt.legend(loc='upper right')

# Display the plot
plt.tight_layout()
plt.show()
'''
