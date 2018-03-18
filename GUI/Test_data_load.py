from Data import *
import matplotlib.pyplot as plt
list = loadObjects('Data_backend.txt')

dates = []
angles = []
for i in range(0,len(list)):
    dates.append(list[i].Date)
    angles.append(list[i].Target_A)

plt.plot(dates, angles)
plt.show()

#https://stackoverflow.com/questions/23151612/pyqtgraph-how-to-plot-time-series-date-and-time-on-the-x-axis