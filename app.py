import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Create Raw Data
raw_data = {
    'User_ID': ['U001', 'U001', 'U002', 'U003', 'U004'],
    'App_Name': ['Instagram', 'Instagram', 'WhatsApp', 'TikTok', 'Candy Crush'],
    'Screen_Time_Min': [45, 45, None, 120, 15],
    'Battery_Drain_Pct': [12, 12, 5, 35, 85]
}
df = pd.DataFrame(raw_data)

# 2. Data Cleaning
df_clean = df.drop_duplicates()
mean_time = df_clean['Screen_Time_Min'].mean()
df_clean['Screen_Time_Min'].fillna(mean_time, inplace=True)
df_clean.loc[df_clean['Battery_Drain_Pct'] > 80, 'Battery_Drain_Pct'] = 15

# 3. Create and Save Visualization
plt.figure(figsize=(6, 4))
sns.barplot(x='App_Name', y='Screen_Time_Min', data=df_clean, palette='Set2')
plt.title('App Usage Analytics')
plt.savefig('app_usage_chart.png')  # Saves chart as an image
print("Project successfully executed! Data cleaned and chart saved.")