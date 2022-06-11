import requests
from bs4 import BeautifulSoup
from datetime import date
import time
import json
from csv import writer

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

#Returns list with name of row and price values
def names_and_values(yes_buy, no_buy, yes_sell, no_sell, dataset=use):
    data = []
    x = 2
    while len(dataset) > x:
        row_name = get_value(x, 3, dataset)[1]
        row_yes_buy = get_value(x, yes_buy, dataset)[1]
        row_no_buy = get_value(x, no_buy, dataset)[1]
        row_yes_sell = get_value(x, yes_sell, dataset)[1]
        row_no_sell = get_value(x, no_sell, dataset)[1]
        whole = {"Name": row_name, "Values": {"Yes Buy Value": row_yes_buy, "No Buy Value": row_no_buy, "Yes Sell Value": row_yes_sell, "No Sell Value": row_no_sell, }}
        #whole = [row_name, [row_yes_buy, row_no_buy, row_yes_sell, row_no_sell]]
        data.append(whole)
        x+=1
    return(data)

def get_date():
    return str(date.today())

def get_time():
    return str(time.strftime("%H:%M:%S"))

#Statement which is to be inserted into JSON file
to_insert = {
get_title(): {
"Date": get_date(),
"Time": get_time(),
"Contents": names_and_values(7,8,9,10)
}
}

#Opens and inserts data into JSON file
with open('saved.json', 'w+') as json_data:
       json.dump(to_insert, json_data, indent=4)
