import pandas as pd
import matplotlib.pyplot as plt
import os

#Global variables
fields = ["ContractName", "Date","OpenSharePrice","CloseSharePrice","LowSharePrice","HighSharePrice","TradeVolume"]

#import CSV file as pandas dataframe
def get_csv(main):
    df = pd.read_csv("CSVs/" + main + '.csv')
    return df

#find unique contract values and returns list sorted by names
def make_contract_types(frame):
    contract_types = frame.ContractName.unique()
    contract_types.sort()
    return contract_types

#returns simple list correspending to contracts
def make_contract_nums(contract_types):
    contract_num_list = [*range(0, len(contract_types), 1)]
    contract_num_list.append(contract_num_list[-1])
    return contract_num_list

#creates a list corresponding to contract name, turns strings into numbers
def convert_row(n, field, number, frame):
    x = frame.loc[frame['ContractName'] == n][field].tolist()
    y = []
    if number == 1:
        for q in x:
            y.append(float(q.strip("$")))
        return y
    elif number == 2:
        for q in x:
            y.append(int(q))
        return y
    return x

#creates layered list formatted [[Contract Name(0),[Date(1)],[Open(2)],[Close(3)],[Low(4)],[High(5)],[Volume(6)]],[...]]
def create_big_list(contract_types, frame):
    all = []
    z = 0
    for n in contract_types:
        q = contract_types[z]
        dates = convert_row(n, "Date", 0, frame)
        opens = convert_row(n, "OpenSharePrice", 1, frame)
        closes = convert_row(n, "CloseSharePrice", 1, frame)
        lows = convert_row(n, "LowSharePrice", 1, frame)
        highs = convert_row(n, "HighSharePrice", 1, frame)
        volumes = convert_row(n, "TradeVolume", 2, frame)
        all.append([n,dates,opens,closes,lows,highs,volumes])
        z += 1
    return all

#creates the graph from the list
def make_graph(contracts, contract_names, field, day_list, sheet, dataset = all):
    color_inc = 0
    colors = ["#ff0000","#aa0000","#330000","#00ff00","#00aa00","#003300","#0000ff","#0000aa","#000033"]
    for n in contracts:
        plt.plot(day_list, dataset[n][field], label=contract_names[n], color=colors[n])
        plt.title(str(sheet))
        plt.xlabel('Days')
        plt.ylabel('Trading Price')
        plt.legend(loc='upper center', prop={'size': 7})
        color_inc -= 1
    if sheet[-1] == "R":
        plt.savefig("Saved_Graphs/RC/" + sheet + "-" + fields[field] + ".png")
    elif sheet[-1] == "5":
        plt.savefig("Saved_Graphs/538/" + sheet + "-" + fields[field] + ".png")

#combines all to get data and save graph
def do_all_graph(main):
    df = get_csv(main)
    contract_types = make_contract_types(df)
    contract_num_list = make_contract_nums(contract_types)
    all = create_big_list(contract_types, df)
    days = [*range(0, len(all[0][2]), 1)] 
    make_graph(contract_num_list, contract_types, 3, days, main, all)
    plt.close("all")
    print("Done" + main)

#reads contents of CSVs folder and gets rid of .csv part, returns list
def read_contents(spesific):
    x = os.listdir("CSVs/")
    final = []
    if spesific == "R":
        for n in x:
            if n[5] == "R":
                final.append(n[0:6])
    elif spesific == "5":
        for n in x:
            if n[5] == "5":
                final.append(n[0:6])
    else:
        for n in x:
            final.append(n[0:6])
    return final

#performs do_all (graph creation and neccessary steps) for all items from read_contents()
def do_multiple_graphs(which):
    for n in which:
        do_all_graph(n)

#did the creation of all graphs with this command
#dre = read_contents()
#do_multiple_graphs(dre)
