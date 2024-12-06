#  Meteor Data Analysis
#  Creator: ME
#  Status: Incomplete

import requests
import matplotlib.pyplot as plt
import copy


#  https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/data_preview
#  NASA
# URL = "https://data.nasa.gov/resource/gh4g-9sfh.json?$query=SELECT%20%60name%60%2C%20%60id%60%2C%20%60nametype%60%2C%20%60recclass%60%2C%20%60mass%60%2C%20%60fall%60%2C%20%60year%60%0AWHERE%0A%20%20%60year%60%0A%20%20%20%20BETWEEN%20%222000-01-01T19%3A03%3A08%22%20%3A%3A%20floating_timestamp%0A%20%20%20%20AND%20%222024-10-04T19%3A03%3A08%22%20%3A%3A%20floating_timestamp%0AORDER%20BY%20%60year%60%20DESC%20NULL%20LAST"
# response = requests.get(URL)
# data = response.json()

#  Sort Data
first_index = 0
last_index = 10
# x = [arr["name"] for arr in data[first_index:last_index]]
# y = [arr["mass"] for arr in data[first_index:last_index]]
# print(x)
# print(y)


# Test Data
x = ['Northwest Africa 7812', 'Northwest Africa 7856', 'Northwest Africa 7862', 'Northwest Africa 7755', 'Northwest Africa 7822', 'Northwest Africa 7858', 'Northwest Africa 7857', 'Northwest Africa 7855', 'Northwest Africa 7861', 'Northwest Africa 7863']
y = ['46.2', '517', '317', '30', '45.8', '459', '246', '916', '611', '1000']
largest_mass = [float(i) for i in copy.deepcopy(y)]
largest_mass.sort()
largest_mass = largest_mass[-1]
        # plt.title()
        # plt.xlabel()
        # plt.ylabel()
        # plt.rc("xlabel", **font)
        # plt.rc("ylabel", **font)
        # plt.text(1, 10, "text")
        # plt.xscale(100)
        # plt.yscale(1000)
        # plt.bar(x, y)



# https://matplotlib.org/stable/users/explain/axes/autoscale.html
        #  Table Contents
# fig, ax = plt.subplots(figsize=(4,20))
fig, ax = plt.subplots()
bar = ax.bar(x, y, edgecolor="red", linewidth=0.7, bottom=0)
# ax.bar(x, range(0, int(largest_mass), 10),edgecolor="white", linewidth=0.7, bottom=0, data=y)
# ax.set_ybound(0, largest_mass - 100)



        #  Table and Window size
fig.tight_layout(pad=10)  #  https://stackoverflow.com/questions/42281851/how-to-add-padding-to-a-plot-in-python
fig.set_size_inches(10, 5)
# fig.set_figwidth(1)
# fig.set_figheight(2)
# fig.subplots_adjust(top=1, bottom=0.5)


        #  Heading Text, Size, and Rotation
ax.set_title("Meteor Masses")
ax.set_xlabel("Name")
ax.set_ylabel("Mass")
ax.xaxis.set_ticks_position("bottom")  # Decides whether text is at the top or bottom of the graph
# ax.set_xlabel("Name", fontsize=4)
# ax.set_xticklabels(x, fontsize=4)  #  Changes the size of the text, but breaks the X value of the bar chart when hovering over it.
ax.tick_params(axis='x',
                which='major',
                labelsize=10,  #  Changes text size
                labelrotation= 90.0,  #  Rotates text
                )  #  https://stackoverflow.com/questions/6390393/how-to-change-tick-label-font-size


        #  X & Y labels on the Bar Chart
# ax.set_ylim((0, 10))
# ax.axis([-1, len(x), 0, len(y)])
# ax.set(ylim=(0, 10), yticks=(0, 9))
# ax.set_xlim((0, 5))


        #  Tables
# table = ax.table(cellText=x, cellLoc="left", rowLabels=y)


plt.show()