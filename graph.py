import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import math

# Load your CSV data
data = pd.read_csv('data.csv', parse_dates=['date'])

# Sort data by date if not already sorted
data.sort_values('date', inplace=True)

# Set the date column as the index
data.set_index('date', inplace=True)

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['modules'])

# Calculate interval for 10 evenly-spaced date labels in date range
date_range = (data.index.max() - data.index.min()).days
interval = max(1, math.ceil(date_range / 10))  # Ensure interval is at least 1

# Formatting the date on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=interval))
plt.gcf().autofmt_xdate()  # Rotate date labels

# Get the most recent value
most_recent_value = data['modules'].iloc[-1]

# Coordinates to place the text (adjust as needed)
x_coord = data.index[-1]  # Get the last date from the index
y_coord = max(data['modules']) * 0.8  # Adjust y-coordinate as needed

# Display the most recent value in the graph
plt.text(x_coord, y_coord, str(most_recent_value), fontsize=20, ha='center')

# Additional formatting (optional)
plt.title('Daggerverse Modules')
plt.xlabel('Date')
plt.ylabel('Modules')

plt.savefig('graph.png')
