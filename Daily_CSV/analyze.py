from numpy import average
from lists import data5
from lists import dataR
import pandas as pd
import numpy as np

def summarize(input):
    final = {"count" : len(input) , "Maximum" : max(input) , "Minimum" : min(input) , "Average" : np.round(average(input),3) , "25th Percentile" : np.round(np.percentile(input,25),3) , "75th Percentile" : np.round(np.percentile(input,75),3)}
    return final

#FORMAT OF THE LIST
# data[0] = cycle ; data[0][0] = contract ; data[0][0][0] = data over a week ; data[0][0][0][0] = data on a given day
# [[Contract Name(0),[Date(1)],[Open(2)],[Close(3)],[Low(4)],[High(5)],[Volume(6)]],[...]]

purchase_prices = []
sale_prices = []
portfolio = []
total_length = []
purchase_and_sale = []
low_param = 0.05
high_param = 0.2
day = -2
wins = 0
losses = 0
for p in data5:
        for n in p[:-1]:
            buy = n[3][day]
            sell = n[3][-1]
            total_length.append("1")
            if (buy > low_param and buy < high_param):
                portfolio.append([buy,sell])
                purchase_prices.append(buy)
                sale_prices.append(sell)
                if sell > 0.9:
                    wins += 1
                else:
                    losses += 1

print("Buy " + str((day+1)*-1) + " days before close if above " + str(low_param) + " but not above " + str(high_param) + ":")
print("Wins: " + str(wins))
print("Losses: " + str(losses))
print("Length: " + str(len(portfolio)) + " / " + str(len(total_length)))
print("Average purchase price: " + str(np.round(average(purchase_prices),3)))
print("Average sale price: " + str(np.round(average(sale_prices),3)))
