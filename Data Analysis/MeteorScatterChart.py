#  Meteor Scatter Chart
#  Creator: ME
#  Status:  Incomplete

from matplotlib import pyplot as plt
import copy, re, requests



#  https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh/data_preview
#  NASA
URL = "https://data.nasa.gov/resource/gh4g-9sfh.json?$query=SELECT%20%60name%60%2C%20%60id%60%2C%20%60nametype%60%2C%20%60recclass%60%2C%20%60mass%60%2C%20%60fall%60%2C%20%60year%60%0AWHERE%0A%20%20%60year%60%0A%20%20%20%20BETWEEN%20%222000-01-01T19%3A03%3A08%22%20%3A%3A%20floating_timestamp%0A%20%20%20%20AND%20%222024-10-04T19%3A03%3A08%22%20%3A%3A%20floating_timestamp%0AORDER%20BY%20%60year%60%20DESC%20NULL%20LAST"
response = requests.get(URL)
data = response.json()

#  Sort Data
first_index = 0
last_index = 10
# x = [arr["name"] for arr in data[first_index:last_index]]
# y = [arr["mass"] for arr in data[first_index:last_index]]
x = [arr["name"] for arr in data]
y = [arr["mass"] for arr in data]


# x = ['Northwest Africa 7812', 'Northwest Africa 7856', 'Northwest Africa 7862', 'Northwest Africa 7755', 'Northwest Africa 7822', 'Northwest Africa 7858', 'Northwest Africa 7857', 'Northwest Africa 7855', 'Northwest Africa 7861', 'Northwest Africa 7863']
# y = ['46.2', '517', '317', '30', '45.8', '459', '246', '916', '611', '1000']

# data = {}
# for index, name in enumerate(x):
#     a = re.split("\s?[0-9]*\Z", name)
#     b = a[0]
#     if b not in data:
#         data[b] = [y[index]]
#     else:
#         data[b].append(y[index])
# print(data)
# print(y)
# largest_mass = [float(i) for i in copy.deepcopy(y)]
# largest_mass.sort()
# largest_mass = largest_mass[-1]


fig, ax = plt.subplots()
fig.tight_layout(pad=10)
fig.set_size_inches(5, 5)


# i = str(x[0])*10
# i = [x[0]]*10
# print(i)
# print("-----")


x = [re.split("\s?[0-9]*\Z", i)[0] for i in x]
y = [float(i) for i in y]
div = 100
# scale = [i/div for i in y if i >= 1000]
scale = [i/div for i in y]

ax.scatter(x,
           y,
           s=scale,
           alpha=0.5
           )
ax.tick_params(axis='x',
                which='major',
                labelsize=10,  #  Changes text size
                labelrotation= 90.0,  #  Rotates text
                ) 
ax.grid()
plt.show()