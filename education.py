import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = r"C:\Users\asus\Documents\cas2.csv"
df = pd.read_csv(file_path, encoding='ISO-8859-1')  # Make sure the file path and encoding are correct

# 8. Percentage of insured vs. non-insured bikes in each state ---
top_states = df["State"].value_counts().nlargest(5).index
df_top = df[df["State"].isin(top_states)]

# Pivot table: count bikes by insurance status per state
df_pivot = df_top.pivot_table(index="State", columns="Insurance Status", values="Brand", aggfunc="count", fill_value=0)

# Convert counts to percentages
df_pivot_percent = df_pivot.div(df_pivot.sum(axis=1), axis=0) * 100

# Plot: Stacked Bar Chart
plt.figure(figsize=(12, 6))
df_pivot_percent.plot(kind="bar", stacked=True, colormap="tab10", figsize=(12, 6))
plt.xlabel("State")
plt.ylabel("Percentage of Bikes (%)")
plt.title("Insured vs. Non-Insured Bikes in Top 5 States")
plt.legend(title="Insurance Status")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 9. Fuel Type & Engine Capacity Analysis ---
fuel_counts = df["Fuel Type"].value_counts()

# Plot: Fuel Type (corrected)
plt.figure(figsize=(8, 5))
sns.barplot(x=fuel_counts.index, y=fuel_counts.values, color='blue')  # Fixed: Using color instead of palette
plt.title("Bike Count by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Number of Bikes")
plt.tight_layout()
plt.show()

#10. Number of bikes sold per state ---
state_counts = df["State"].value_counts()

# Plot: Bikes Sold per State (corrected)
plt.figure(figsize=(12, 6))
sns.barplot(x=state_counts.index, y=state_counts.values, color='green')  # Fixed: Using color instead of palette
plt.title("Number of Bikes Sold per State")
plt.xlabel("State")
plt.ylabel("Number of Bikes Sold")
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()

#11. Correlation Heatmap of Numerical Features
num_features = ['Price (INR)', 'Engine Capacity (cc)', 'Mileage (km/l)', 
                'Resale Price (INR)', 'Avg Daily Distance (km)']
corr = df[num_features].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Numerical Features')
plt.tight_layout()
plt.show()

#12. Average Price & Resale Price Over Years
avg_price_by_year = df.groupby('Year of Manufacture')[['Price (INR)', 'Resale Price (INR)']].mean()

plt.figure(figsize=(10, 6))
avg_price_by_year.plot(kind='line', marker='o')
plt.title('Average Price and Resale Price Over Years')
plt.xlabel('Year of Manufacture')
plt.ylabel('Price (INR)')
plt.legend(["Avg Price", "Avg Resale Price"])
plt.grid(True)
plt.tight_layout()
plt.show()
