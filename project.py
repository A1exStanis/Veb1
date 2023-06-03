# Create a module plotter.py that takes a list of numbers as input and uses matplotlib to generate a line plot. 
# Generate a graph for the UAH/USD exchange rate since 2000.
import tkinter
from datetime import datetime
import matplotlib.pyplot as plt
import csv

dates = []
rates = []

with open("Files3/target.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Date"])
        dates.append(datetime.strptime(row["Date"], '%Y-%m-%d'))
        rates.append(float(row["Rate"]))
plt.style.use('_mpl-gallery')

fig, ax = plt.subplots()

ax.plot(dates, rates, linewidth=2.0)


plt.show()