# Cognitive bias parcer

from bs4 import BeautifulSoup as soup
import requests
import csv
# urllib2 - This library is apparently a no go.

wiki_url = "https://en.wikipedia.org/wiki/Cognitive_bias"


req = requests.get(wiki_url)
req.status_code == requests.codes.ok  # Checks it request was successful. 200 means Success. 404 means Unsuccessful.

try:
    req.raise_for_status()  # Returns error if the code was unsuccessful (404)
    print(type(req))
    testSoup = soup(req.text, "html.parser")
    print(type(testSoup))
    #content = testSoup.select(".wikitable")
    #print(type(content))
except Exception as err:
    print("Problem encountered: %s" % err)

# TODO: Format the contents. Filter: Wikitable > Filter: tr > Filters: td


testSoup = testSoup.findAll("table", {"class" : "wikitable"})  # Finds table values.
print(testSoup)

testSoup = testSoup[1]  # Gets the first value
all_rows = testSoup.find_all("tr")  # Breaks the table into the tr contents.
data = all_rows[1:]  # Ignores the header.
print(data[0])  # Prints the first value.

data_rows = []
for row in data:
    data_row = []
    row.find_all("td")  # Gets all table data
    for datapoint in row:
        if datapoint.text[:-1] == "":  # Removes data points.
            pass
        else:
            data_row.append(datapoint.text[:-1])  # Removes \n
    data_rows.append(data_row)  # Adds new data points
print(len(data_rows))

for i in range(len(data_rows)):
    print("Length: ", len(data_rows[i]))

print(data_rows[0][1])

'''
data_rows = []
for row in data:
    data_row = []
    row.find_all("td")
    for datapoint in row:
        data_row.append(datapoint.text[:-1])
    data_rows.append(data_row)
print(data_rows)
'''

# TODO: Save File as CSV
''' Works
for data in data_rows:
    print({data[0] : data[1]})
'''
with open("Cognitive Bias.csv", "w", newline="") as f:
    fieldnames = ["Cognitive Bias", "Description"]
    writer = csv.DictWriter(f, fieldnames = fieldnames)  # Assigns file and fieldnames.
    for data in data_rows:
        writer.writerow({"Cognitive Bias" : str(data[0]), "Description" : str(data[1])})  # Adds rows. Values assigned to field names.
    
        
    
