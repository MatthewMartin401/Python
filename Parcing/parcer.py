# parcer

from bs4 import BeautifulSoup as soup
import requests
import csv

wiki_url = ""  # URL Parce Target.

req = requests.get(wiki_url)  # Gets URL Page Contents.
req.status_code == requests.codes.ok  # Checks it request was successful. 200 means Success. 404 means Unsuccessful.

try:
    req.raise_for_status()  # Returns error if the code was unsuccessful (404)
    testSoup = soup(req.text, "html.parser")  # Gets all the text.
except Exception as err:
    print("Problem encountered: %s" % err)  # Print the Exception Error encountered.

testSoup = testSoup.findAll("table", {"class" : str(input("class name"))})  # Finds table values.
print(testSoup)  # Prints all collected text.

testSoup = testSoup[1]  # Gets the first value
all_rows = testSoup.find_all("tr")  # Breaks the table into the tr tag contents.
data = all_rows[1:]  # Ignores the header.
print(data[0])  # Prints the first value.

data_rows = []
for row in data:
    data_row = []  # Empties contents.
    row.find_all("td")  # Gets all table data
    for datapoint in row:  # Gets all data from row.
        if datapoint.text[:-1] == "":  # Removes data points that are emptpy.
            pass
        else:
            data_row.append(datapoint.text[:-1])  # Adds data point with the \n removed.
    data_rows.append(data_row)  # Adds new data points
print(len(data_rows))  # Number of rows.

for i in range(len(data_rows)):
    print("Length: ", len(data_rows[i]))  # Number of data points in row.

print(data_rows[0][1])  # Prints first rows second value.

with open("Filename.csv", "w", newline="") as f:  # Creates CSV File.
    fieldnames = ["Column 1", "Column 2"]  # Creates filenames.
    writer = csv.DictWriter(f, fieldnames = fieldnames)  # Assigns file and fieldnames.
    for data in data_rows:
        writer.writerow({"Column 1" : str(data[0]), "Column 2" : str(data[1])})  # Adds rows. Values assigned to field names.
    
        
    
