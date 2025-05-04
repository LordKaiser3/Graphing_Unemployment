from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Read the CSV file and parse the data
path = Path('OHUR.csv')
lines = path.read_text(encoding='utf-8').splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Get the header row to see the column names
for index, column_header in enumerate(header_row):
    print(f"{index}: {column_header}, ", end=' ')
print()

# Get the index of the date and unemployment rate columns
date = []
unemployment_rate = []

for row in reader:
    date.append(datetime.strptime(row[0], "%Y-%m-%d"))
    unemployment_rate.append(float(row[1]))

# set the figure size and plot the unemployment rate
plt.figure(figsize=(10, 5))
plt.plot(date, unemployment_rate, label="Unemployment Rate", color="blue")

# Lavel the graph's axes and title
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.title("National Unemployment Rate Over Time")
plt.legend()

# Show the grid and plot it
plt.grid()
plt.show()
