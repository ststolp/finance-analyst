import sys  
import pandas as pd 
import numpy as np
from dateutil.parser import parse
# startDate = sys.argv[1]
# endDate = sys.argv[2]
# now = sys.argv[3]
millisecondDay = 86400000

# Spread x values every 15 days
interval = millisecondDay * 15
types = ['salary', 'bonus', 'commision', 'child support', 'interest']
categories =  ['home', 'auto', 'food', 'entertainment', 'phone', 'internet', 'water', 'gas', 'charity',
'electric', 'miscellaneous']
methods = ['Cash', 'Credit', 'Debit', 'Check']
# The number of records to fabricate
num_fake_records = 10000
# random number generator
rng = np.random.default_rng()

def generateColumn(column, num = 100):
    indexes = rng.integers(0, len(column), size=num)
    resultList = []
    for i in indexes:
        resultList.append(column[i])
    return resultList

def generateDates(min_date, max_date):
    dates = []
    return dates

test = ['6/7/2019', '7/7/2018', '5/30/1997']
testtime = pd.to_datetime(test)
print(testtime)
methodsColumn = generateColumn(methods, num_fake_records)
typesColumn = generateColumn(types, num_fake_records)
catsColumn = generateColumn(categories, num_fake_records)
# datesColumn = generateDates(startDate, endDate)
# Get the dataFrame for actual income and expense transactions
expense_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/expense.csv')
income_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/income.csv')
expense_df['date'] = pd.to_datetime(expense_df['date'])
# print(expense_df)
# print(income_df)

# generate fabricated dataframe

# TODO: fabricate the Dates, don't bother with payment_to or description
# expense_df_test = pd.DataFrame({'date': datesColumn, 'method': methodsColumn, 'category': catsColumn,
#                                'amount': rng.integers(1, 500, size = num_fake_records)})

# print(expense_df_test)
# generate the stuff
# ....
# interval = 50
# startDate = 0
# endDate = 300
# now = 200
#x = list(range(startDate, endDate, interval))

total_income = []
home = []
auto = []
food = []
entertainment = []
misc = []
charity = []
water = []
gas = []
electric = []
internet = []
phone = []
# for testing purposes
x = [2015, 2016, 2017, 2018]

#for i in x: 
    #if i == startDate:
    #    continue
    #elif i > now:
        #print("elif")
        # incomeSum = # some forecast
        # incomeY.append(incomeSum)
    #else:
        #print("else..")
        # from data
        # incomeSum = ?
        # incomeY.append(incomeSum)
    #...calc for each category

# iterate through x list, get sums for the time interval, push them onto their respective y list
#print(expense_df['amount'].groupby(expense_df['category']).sum())
expense_sums = expense_df['amount'].groupby(expense_df['category']).sum()
# print(expense_sums)
# income_sums = list(income_df['amount'].groupby(income_df['type']).sum())

# print(expense_df[0])
# for expenseType in types:
#     print(expense_sums[expenseType])

# for cat in cats:
#     print(income_sums[cat])

# income type: salary, bonus, commision, child support, interest  #
# income cats: home, auto, food, entertainment, phone, internet, water, gas, charity, electric, miscellaneous

# lets pretend we have the stuff, for testing purposes
# return json object string

total_income = [5000, 6000, 9000, 8000]
home = [800, 750, 1820, 930]
auto = [300, 300, 600, 300]
food = [500, 400, 450, 515]
entertainment = [100, 110, 120, 130]
misc = [130, 120, 110, 100]
charity = [150, 130, 100, 50]
water = [20, 25, 26, 27]
gas = [80, 85, 75, 70]
electric = [10, 20, 25, 30]
internet = [30, 25, 20, 10]
phone = [45, 90, 45, 80]

# print('{"income": {"x": ')
# print(x)
# print(', "y": ')
# print(total_income)
# print(', "type": "scatter", "name": "Total Income"}, "home": {"x": ')
# print(x)
# print(',"y": ')
# print(home)
# print(', "type": "scatter", "name": "Home"}, "auto": {"x": ')
# print(x)
# print(',"y": ')
# print(auto)
# print(', "type": "scatter", "name": "Auto"}, "food": {"x": ')
# print(x)
# print(',"y": ')
# print(food)
# print(', "type": "scatter", "name": "Food"}, "entertainment": {"x": ')
# print(x)
# print(',"y": ')
# print(entertainment)
# print(', "type": "scatter", "name": "Entertainment"}, "miscellaneous": {"x": ')
# print(x)
# print(',"y": ')
# print(misc)
# print(', "type": "scatter", "name": "Miscellaneous"}, "charity": {"x": ')
# print(x)
# print(',"y": ')
# print(charity)
# print(', "type": "scatter", "name": "Charity"}, "water": {"x": ')
# print(x)
# print(',"y": ')
# print(water)
# print(', "type": "scatter", "name": "Water"}, "gas": {"x": ')
# print(x)
# print(',"y": ')
# print(gas)
# print(', "type": "scatter", "name": "Gas"}, "electric": {"x": ')
# print(x)
# print(',"y": ')
# print(electric)
# print(', "type": "scatter", "name": "Electric"}, "internet": {"x": ')
# print(x)
# print(',"y": ')
# print(internet)
# print(', "type": "scatter", "name": "Internet"}, "phone": {"x": ')
# print(x)
# print(',"y": ')
# print(', "type": "scatter", "name": "Phone"}}')
