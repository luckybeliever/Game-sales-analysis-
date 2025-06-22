import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
file_path = "Game_sales_cleaned.csv"  # Make sure this file is in the same directory
df = pd.read_csv(file_path)

# Get unique genres
genre_list = sorted(df['Genre'].dropna().unique().tolist())

# Display available genres
print("Available genres:")
for idx, genre in enumerate(genre_list, start=1):
    print(f"{idx}. {genre}")

# Ask user to choose a genre
selected_genre = input("\nEnter the genre exactly as shown above: ")

# Validate genre input
if selected_genre not in genre_list:
    print("Invalid genre selected. Please run the program again and enter a valid genre.")
    exit()

# Filter data by selected genre
filtered_df = df[df['Genre'] == selected_genre]

# Group by Publisher and sum Global Sales
publisher_sales = (
    filtered_df.groupby("Publisher")["Global_Sales"]
    .sum()
    .reset_index()
    .sort_values(by="Global_Sales", ascending=False)
)

# Get Top 5 and calculate 'Other'
top5 = publisher_sales.head(5)
other_sales = publisher_sales.iloc[5:]["Global_Sales"].sum()

# Combine Top 5 with 'Other'
top5_plus_other = pd.concat(
    [top5, pd.DataFrame([{"Publisher": "Other", "Global_Sales": other_sales}])],
    ignore_index=True
)

# Plot pie chart
plt.figure(figsize=(8, 6))
plt.pie(
    top5_plus_other["Global_Sales"],
    labels=top5_plus_other["Publisher"],
    autopct="%1.1f%%",
    startangle=140
)
plt.title(f"Top 5 Publishers + Other for Genre: {selected_genre}")
plt.axis("equal")
plt.tight_layout()
plt.show()
