import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load your CSV data
data = pd.read_csv('data.csv', parse_dates=['date'])

# Sort data by date if not already sorted
data.sort_values('date', inplace=True)

# Set the date column as the index
data.set_index('date', inplace=True)

# Plotting the data
plt.figure(figsize=(10, 5))
plt.plot(data.index, data['modules'])

# Formatting the date on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Format the date display
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))  # Set interval (change '5' to your desired interval)

plt.gcf().autofmt_xdate()  # Rotate date labels

# Additional formatting (optional)
plt.title('Daggerverse Modules')
plt.xlabel('Date')
plt.ylabel('Modules')

plt.savefig('graph.png')
