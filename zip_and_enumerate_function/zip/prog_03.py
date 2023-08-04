# python zip() dictionary
stocks = ['Reliance', 'Infosys', 'TCS']
prices = [2175, 1127, 2750]
new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}  # dict comprehension
print(new_dict)