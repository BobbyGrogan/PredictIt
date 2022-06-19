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
wins = 0
losses = 0
for p in dataR:
        for n in p[:-1]:
            buy = n[3][-2]
            sell = n[3][-1]
            total_length.append("1")
            if (buy > 0.2 and buy < 0.5):
                portfolio.append([buy,sell])
                purchase_prices.append(buy)
                sale_prices.append(sell)
                if sell > 0.9:
                    wins += 1
                else:
                    losses += 1

print(portfolio)
print("Wins: " + str(wins))
print("Losses: " + str(losses))
print("Length: " + str(len(portfolio)) + " / " + str(len(total_length)))
print("Average purchase price: " + str(np.round(average(purchase_prices),3)))
print("Average sale price: " + str(np.round(average(sale_prices),3)))


# for n in portfolio:
#     dif = np.round((n[1] - n[0])/n[0],3)
#     purchase_and_sale.append(dif)

# print("Ratio: " + str(np.round(wins/losses, 3)))
# print("Average gain: " + str(np.round(average(purchase_and_sale),3)))





#IGNORE BELOW

# blah = []
# all_results = []
# portfolio = []
# for p in dataR:
#     for n in p[:-1]:
#         blah.append("1")
#         if n[3][-3] > 0.2 and n[3][-3] < 0.4:
#             portfolio.append([n[3][-3],n[3][-1]])

# for n in portfolio:
#     dif = np.round((n[1] - n[0])/n[0],3)
#     all_results.append(dif)
    

# print(all_results)
# print(summarize(all_results))

# print("\n")
    
# pd_index_results = pd.Series(index_results)
# print(pd_index_results.value_counts())
