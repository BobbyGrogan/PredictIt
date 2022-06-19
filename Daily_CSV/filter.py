from numpy import average
from lists import data5
from lists import dataR
import pandas as pd
import numpy as np

def summarize(input):
    final = {"count" : len(input) , "Maximum" : max(input) , "Minimum" : min(input) , "Average" : np.round(average(input),3) , "25th Percentile" : np.percentile(input,25) , "75th Percentile" : np.percentile(input,75)}
    return final

# data[0] = cycle ; data[0][0] = contract ; data[0][0][0] = data over a week ; data[0][0][0][0] = data on a given day
# [[Contract Name(0),[Date(1)],[Open(2)],[Close(3)],[Low(4)],[High(5)],[Volume(6)]],[...]]

win_results = []
all_results = []
portfolio = []
for p in data5:
    for n in p[:-1]:
        if n[3][-3] > 0.2 and n[3][-3] < 0.5:
            portfolio.append([n[3][-3],n[3][-1]])

for n in portfolio:
    dif = np.round((n[1] - n[0])/n[0],3)
    all_results.append(dif)
    

print(all_results)
print(summarize(all_results))

# print("\n")
    
# pd_index_results = pd.Series(index_results)
# print(pd_index_results.value_counts())
