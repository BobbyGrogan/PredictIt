from click import option
from matplotlib.pyplot import xlim
import requests
from bs4 import BeautifulSoup

#Biden 538 approval rating June 15th
which_market = "7973"                           #str(input("ID for market? : "))

#Gets data form PredictIt API
req = requests.get("https://www.predictit.org/api/marketdata/markets/" + which_market)
soup = BeautifulSoup(req.content, "html.parser")

use = str(soup).split('{')

#Returns title of subject
def get_title(dataset=use):
    title = (dataset[1].split(",")[1]).split('"')[3]
    return(title)

#Returns individual value
def get_value(row, cell, dataset=use):
    got = (dataset[row]).split(",")[cell]
    cell_name = got.split(":")[0].replace("\r\n","").replace(" ","").replace('"',"")
    cell_value = got.split(":")[1].replace(" ","").replace('"','')
    both = [cell_name, cell_value]
    return(both)

#Returns the title and number of betting options
def overall(dataset=use):
    length = len(dataset) - 2
    all = [get_title(dataset), str(length) + " Options"]
    return(all)

#Returns the names of the various options
def option_names(dataset=use):
    names = []
    x = 2
    while len(dataset) > x:
        names.append(get_value(x, 3, dataset)[1])
        x+=1
    return(names)

import json
to_insert = {
"Title": get_title()
}
with open('saved.json', 'w') as json_data:
    json.dump(to_insert, json_data)