import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("earthquake.csv")

# Show basic info
print("✅ Data loaded successfully!\n")
print(data.head())
print("\nColumns available:", list(data.columns))

# --- 1️⃣ Number of Earthquakes Per Year ---
plt.figure(figsize=(10,5))
sns.countplot(x='Year', data=data, hue='Year', palette='viridis', legend=False)
plt.title("Number of Earthquakes Per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- 2️⃣ Average Magnitude Per Year ---
plt.figure(figsize=(10,5))
avg_mag = data.groupby('Year')['magnitude'].mean().reset_index()
sns.lineplot(x='Year', y='magnitude', data=avg_mag, marker='o', color='red')
plt.title("Average Earthquake Magnitude Per Year")
plt.tight_layout()
plt.show()

# --- 3️⃣ Tsunamis Per Year ---
plt.figure(figsize=(10,5))
tsunami_counts = data.groupby('Year')['tsunami'].sum().reset_index()
sns.barplot(x='Year', y='tsunami', data=tsunami_counts, hue='Year', palette='coolwarm', legend=False)
plt.title("Number of Tsunamis Per Year")
plt.tight_layout()
plt.show()

# --- 4️⃣ Magnitude vs Depth ---
plt.figure(figsize=(8,5))
sns.scatterplot(x='depth', y='magnitude', data=data, hue='tsunami', palette='coolwarm')
plt.title("Magnitude vs Depth (Color shows if Tsunami occurred)")
plt.tight_layout()
plt.show()
