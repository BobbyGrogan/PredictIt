import requests
from bs4 import BeautifulSoup
from datetime import date
import time
import csv
from csv import writer

#Gets data form PredictIt API
def get_api(which_market="7956"):
    req = requests.get("https://www.predictit.org/api/marketdata/markets/" + which_market)
    soup = BeautifulSoup(req.content, "html.parser")
    this = str(soup).split('{')
    return this

#Returns title of subject
def get_title(dataset=get_api()):
    title = (dataset[1].split(",")[1]).split('"')[3]
    return(title)

#Returns individual value
def get_value(row, cell, dataset=get_api()):
    got = (dataset[row]).split(",")[cell]
    cell_name = got.split(":")[0].replace("\r\n","").replace(" ","").replace('"',"")
    cell_value = got.split(":")[1].replace(" ","").replace('"','')
    both = [cell_name, cell_value]
    return(both)

#Returns the title and number of betting options
def overall(dataset=get_api()):
    length = len(dataset) - 2
    all = [get_title(dataset), str(length) + " Options"]
    return(all)

#Returns the names of the various options
def option_names(dataset=get_api()):
    names = []
    x = 2
    while len(dataset) > x:
        names.append(get_value(x, 3, dataset)[1])
        x+=1
    return(names)

#Returns the current date as a string in 'YEAR-MN-DT' format
def get_date():
    return str(date.today())

#Returns the current time as a string in 'HR:MN:SC' format
def get_time():
    return str(time.strftime("%H:%M:%S"))

#Returns list with values for rows in CSV
def get_values(yes_buy=7, no_buy=8, yes_sell=9, no_sell=10, dataset=get_api()):
    values = [get_title(), get_date(), get_time()]
    x = 2
    while len(dataset) > x:
        row_name = get_value(x, 3, dataset)[1]
        row_yes_buy = get_value(x, yes_buy, dataset)[1]
        row_no_buy = get_value(x, no_buy, dataset)[1]
        row_yes_sell = get_value(x, yes_sell, dataset)[1]
        row_no_sell = get_value(x, no_sell, dataset)[1]
        whole = [row_yes_buy, row_no_buy, row_yes_sell, row_no_sell]
        for n in whole:
            values.append(n)
        x+=1
    return(values)

#Returns a list with values for column names for CSV
def get_fields(dataset=get_api()):
    fields = ["Title", "Date", "Time"]
    x = 2
    while len(dataset) > x:
        row_name = get_value(x, 3, dataset)[1]
        whole = ["Buy Yes", "Buy No", "Sell Yes", "Sell No"]
        for n in whole:
            fields.append(str(row_name) + ": " + str(n))
        x+=1
    return(fields)

fields = get_fields()
values = get_values()
filename = "7956.csv"

def format_csv():
    with open(filename, "w") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)

def update_csv():
    with open(filename, "a", newline="") as f:
        writer_object = writer(f)
        writer_object.writerow(values)
        f.close()

def repeat_update():
    x = 1
    while x ==1:
        update_csv()
        print("Updated")
        time.sleep(80)

format_csv()
repeat_update()