import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("/Users/frenwd24/Desktop/AIPython/countries (1).csv") 
print(df.shape)
df = df.dropna()
# Assuming 'df' is your DataFrame and it has columns ['Country', 'Year', 'Population']
# If your DataFrame has different column names, adjust the column references accordingly.

# Step 1: Filter the DataFrame for the countries of interest
us = df[df.country == "United States"]
jp = df[df.country == "Japan"]
de = df[df.country == "Germany"]
cn = df[df.country == "China"]
cu = df[df.country == "Cuba"]

us['percent'] = us['population'].pct_change() * 100
jp['percent'] = jp['population'].pct_change() * 100
de['percent'] = de['population'].pct_change() * 100
cn['percent'] = cn['population'].pct_change() * 100
cu['percent'] = cu['population'].pct_change() * 100

# # Select only the first and last year rows for each country
# us = us.iloc[[0, -1]]  # First and last row for the United States
# jp = jp.iloc[[0, -1]]  # First and last row for Japan
# de = de.iloc[[0, -1]]  # First and last row for Germany
# cn = cn.iloc[[0, -1]]  # First and last row for China
# cu = cu.iloc[[0, -1]]  # First and last row for Cuba
# print(us)

plt.figure(figsize=(10, 6))  # Set the figure size for better readability
plt.plot(us['year'], us['percent'], label=us['country'])
plt.plot(jp['year'], jp['percent'], label=jp['country'])
plt.plot(de['year'], de['percent'], label=de['country'])
plt.plot(cn['year'], cn['percent'], label=cn['country'])
plt.plot(cu['year'], cu['percent'], label=cu['country'])

plt.xlabel('Year')  # X-axis label
plt.ylabel('Population Percent Change')  # Y-axis label
plt.title('Population Growth')  # Chart title
plt.legend()  # Show legend to identify the lines
plt.show()  # Display the plot
'''   
# Plotting
plt.figure(figsize=(10, 6))  # Set the figure size for better readability

for country in ['China', 'United States', 'Japan']:
    country_df = filtered_df[filtered_df['country'] == country]
    plt.plot(country_df['year'], country_df['population'], label=country)

plt.xlabel('Year')  # X-axis label
plt.ylabel('Population')  # Y-axis label
plt.title('Population Growth')  # Chart title
plt.legend()  # Show legend to identify the lines
plt.show()  # Display the plot
'''
