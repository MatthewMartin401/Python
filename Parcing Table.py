#  Parcing Table
#  Creator: ME
#  Complete: True

from matplotlib import pyplot as plt
import requests
from bs4 import BeautifulSoup as soup
import numpy as np
import re

#  Get data
FREEZE_URL = "https://en.wikipedia.org/wiki/Freezing-point_depression"
BOIL_URL = "https://en.wikipedia.org/wiki/Boiling-point_elevation"
# response = requests.get(URL)
# print(response.ok)
# print(response.status_code)

freeze_req = requests.get(FREEZE_URL)
boil_req = requests.get(BOIL_URL)

if freeze_req.ok and boil_req.ok:
    #  Attempt Connection
    try:
        freeze_req.raise_for_status()
        boil_req.raise_for_status
        frez_soup = soup(freeze_req.text, "html.parser")
        boil_soup = soup(boil_req.text, "html.parser")

        # response.raise_for_status()
        # print(response.raise_for_status())
        # testSoup = soup(response.text, "html.parser")
        # print("Here")
    except Exception as err:
        print("Problem encounter %s" % err)
    
    frez_tab = frez_soup.find("table", {"class" : "wikitable"})
    boil_tab = boil_soup.find("table", {"class" : "wikitable"})

    # print(frez_tab.get_text().split("\n"))
    # print(boil_tab.get_text().split("\n"))

    frez_arr = [i for i in frez_tab.get_text().split("\n") if i not in ['']]  #  Removes empty values from the list.
    boil_arr = [i for i in boil_tab.get_text().split("\n") if i not in ['']]

    cols = frez_arr[:2] + [boil_arr[1]]  #  Gets the column names from both data tables.
    print(cols)

    #  Find hyphen minus
    print(chr(ord("−")))  #  Needs to remove the Hyphen Minus, as it only works within a string.
    subbed = re.sub(f"{chr(8722)}", '+', (str(chr(8722))+'100'))
    print(subbed)

    boil_arr = {boil_arr[i] : boil_arr[i+1] for i in range(3, len(boil_arr), 3)}  #  Changes the start location for the values. Also changes the data intervals.
    frez_arr = {frez_arr[i] : frez_arr[i+1] for i in range(3, len(frez_arr), 3)}

    # for val in boil_arr:  #  TODO: There is a problem where the values cannot be converted into floats, as there is a non-convertible string value. Either user .replace or the re library.
        
    # for val in frez_arr:
    #     if "-" in val:
    #         print(True)

    table_data = {i : [float(re.sub(f"{chr(8722)}", '-', frez_arr[i])), float(re.sub(f"{chr(8722)}", '-', boil_arr[i]))] for i in boil_arr if i in frez_arr}  #  Creates a dictionary of Name : [FreezeTemp, BoilTemp]. Also replaces the Hyphen minus with a mathmatical minus.
    print(table_data)

    #  Table Scale
    fig, ax = plt.subplots()
    fig.tight_layout(pad=10)
    fig.set_size_inches(5, 5)
    rows = [i for i in table_data.keys()]
    print([x for x in [i for i in table_data.values()]])
    print(rows)
    ax.bar(rows, height=[i[1] for i in table_data.values()])
    ax.bar(rows, height=[i[0] for i in table_data.values()])
    ax.tick_params('x',
                   labelrotation=90)
    # ax.set_ylim(ymax=,
    #             ymin=)

    for index, bar in enumerate(table_data):
        print(index)
        print(table_data[bar][1], table_data[bar][0])
        # plt.bar(rows, height=table_data[bar][0])
        # plt.bar(rows, height=table_data[bar][0])

    ax.table([i for i in table_data.values()], 
             colLabels=cols[1:], 
             rowLabels=rows, 
             colLoc='center', 
             rowLoc='center',
             cellLoc='center',
             loc='bottom')
    plt.show()
    
    # table_data = []
    # for entry in data:
    #     row = []
    #     for value in entry:
    #         #  Add a value in row
    #         row.append(value)
    #     table_data.append(row)
    # print(table_data)



    # print(boil_arr)
    # print(frez_arr)

    # print(frez_arr[3:])
    # print(boil_arr[3:])

    

    # print(type(testSoup))
    # text = testSoup.find_all("table", {"class" : "wikitable"})

    # ax.table(table_data)
    # ax.table(
    #     [
    #         [1, 0],
    #         [2, 0],
    #         [3, 0]
    #     ]
    # )
    # plt.show()
else:
    print("Problem Encountered: %s" % response.status_code)