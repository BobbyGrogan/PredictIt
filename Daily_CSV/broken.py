# from typing import Final
# from numpy import average
# from lists import data5
# from lists import dataR
# import pandas as pd
# import numpy as np

# def summarize(input):
#     final = {"count" : len(input) , "Maximum" : max(input) , "Minimum" : min(input) , "Average" : np.round(average(input),3) , "25th Percentile" : np.round(np.percentile(input,25),3) , "75th Percentile" : np.round(np.percentile(input,75),3)}
#     return final

# #FORMAT OF THE LIST
# # data[0] = cycle ; data[0][0] = contract ; data[0][0][0] = data over a week ; data[0][0][0][0] = data on a given day
# # [[Contract Name(0),[Date(1)],[Open(2)],[Close(3)],[Low(4)],[High(5)],[Volume(6)]],[...]]

# portfolio = []
# total_length = []
# purchase_and_sale = []
# whole_large = []
# low_params = [0.0,0.05,0.1,0.2,0.3,0.4,0.6,0.8]
# high_params = [0.05,0.1,0.2,0.3,0.4,0.6,0.8,1.0]
# days = [-7,-6,-5,-4,-3,-2]
# wins = 0
# losses = 0

# def results(day, low_param, high_param, wins, losses, purchase_prices, sale_prices):
#     how_many_days_before = (day+1)*-1
#     if_above = low_param
#     if_below = high_param
#     w = wins
#     l = losses
#     number_of_buys = len(purchase_prices)
#     average_purchase_price = None
#     average_sale_price = None
#     average_difference = None
#     if len(purchase_prices) > 0:
#         average_purchase_price = np.round(average(purchase_prices),3)
#     if len(sale_prices) > 0:
#         average_sale_price = np.round(average(sale_prices),3)
#     if len(purchase_prices) > 0 and len(sale_prices) > 0:
#         average_difference = np.round(average_sale_price - average_purchase_price,3)
#     final = [["How many days before: ", how_many_days_before], ["If above: ", if_above], ["If below: ", if_below], ["Wins: ", w], ["Losses: ", l], ["Number of buys: ", number_of_buys], ["Average purchase price: ", average_purchase_price], ["Average sale price: ", average_sale_price], ["Average difference: ", average_difference]]
#     return final

# for p in dataR:
#         for n in p[:-1]:
#             for y in days:
#                 wins = 0
#                 losses = 0
#                 purchase_prices = []
#                 sale_prices = []
#                 buy = n[3][y]
#                 sell = n[3][-1]
#                 for l in low_params:
#                     for h in high_params:
#                         if (buy > l and buy < h):
#                             purchase_prices.append(buy)
#                             sale_prices.append(sell)
#                             if sell > 0.9:
#                                 wins += 1
#                             else:
#                                 losses += 1
#                         whole_large.append(results(y, l, h, wins, losses, purchase_prices, sale_prices))

# def present(slice):
#     for n in slice:
#         print(n[0] + str(n[1]))

# whole_compact = []
# for i in whole_large:
#     if i not in whole_compact:
#         whole_compact.append(i)

# # for p in whole_compact: 
# #     if p[-1][1] > 0.5:
# #         print(p)

# # for n in portfolio:
# #     dif = np.round((n[1] - n[0])/n[0],3)
# #     purchase_and_sale.append(dif)

# # print("Ratio: " + str(np.round(wins/losses, 3)))
# # print("Average gain: " + str(np.round(average(purchase_and_sale),3)))





# #IGNORE BELOW

# # blah = []
# # all_results = []
# # portfolio = []
# # for p in dataR:
# #     for n in p[:-1]:
# #         blah.append("1")
# #         if n[3][-3] > 0.2 and n[3][-3] < 0.4:
# #             portfolio.append([n[3][-3],n[3][-1]])

# # for n in portfolio:
# #     dif = np.round((n[1] - n[0])/n[0],3)
# #     all_results.append(dif)
    

# # print(all_results)
# # print(summarize(all_results))

# # print("\n")
    
# # pd_index_results = pd.Series(index_results)
# # print(pd_index_results.value_counts())
