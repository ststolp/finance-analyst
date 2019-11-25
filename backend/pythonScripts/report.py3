import sys  
import pandas as pd 
import numpy as np
from dateutil.parser import parse
from datetime import datetime

startDate = pd.to_datetime(sys.argv[1])
endDate = pd.to_datetime(sys.argv[2])
now = pd.to_datetime(sys.argv[3])
# startDate = pd.to_datetime('4/1/2019')
# endDate = pd.to_datetime('12/31/2019')
# now = pd.to_datetime('7/4/2019')

types = ['salary', 'bonus', 'commision', 'child support', 'interest']
categories =  ['home', 'auto', 'food', 'entertainment', 'phone', 'internet', 'water', 'gas', 'charity',
'electric', 'miscellaneous']
methods = ['Cash', 'Credit', 'Debit', 'Check']
# The number of records to fabricate
num_fake_records = 100
# random number generator
rng = np.random.default_rng()

def generateColumn(column, num = 100):
    indexes = rng.integers(0, len(column), size=num)
    resultList = []
    for i in indexes:
        resultList.append(column[i])
    return resultList

def generateDates(min_date, max_date):
    dates = pd.date_range(min_date, max_date, periods = num_fake_records, normalize=True)
    return dates

methodsColumn = generateColumn(methods, num_fake_records)
typesColumn = generateColumn(types, num_fake_records)
catsColumn = generateColumn(categories, num_fake_records)
# datesColumn = generateDates(startDate, endDate)
# Get the dataFrame for actual income and expense transactions
expense_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/expense.csv')

# Make the date column into datetimes
expense_df['date'] = pd.to_datetime(expense_df['date'].values)

# Sort the date values ...
expense_df = expense_df.sort_values(by='date')

# ... and make date into the index...
expense_df.index = expense_df['date']

# ... in order to slice the dataframe within the provided date range.
new_expense = expense_df[startDate:endDate]
# print(new_expense)

# expense_df_test = pd.DataFrame({'date': datesColumn, 'method': methodsColumn, 'category': catsColumn,
#                                'amount': rng.integers(1, 500, size = num_fake_records)})

expense_sums = new_expense.pivot_table('amount', index='month', columns='category', aggfunc='sum', fill_value=0)

x = list(range(len(expense_sums.index)))
# expense_sums = expense_df_test.pivot_table('amount', index='month', columns='category', aggfunc='sum', fill_value=0)
# income_sums = income_df_test.pivot_table('amount', index='month', aggfunc='sum', fill_value=0)

# TODO: If now comes before the endDate, Only predict one month in the future based on 
# the trajectory from the last two data samples.
# "Always in motion is the future - Yoda"
# if now < endDate:
    # print('end date is in the future\n')

try:
    total_income = list(expense_sums['income'].values)
except KeyError:
    total_income = [0]
try:
    home = list(expense_sums['home'].values)
except KeyError:
    home = [0]
try: 
    charity = list(expense_sums['charity'].values)
except KeyError:
    charity = [0]
try:   
    water = list(expense_sums['water'].values)
except KeyError:
    water = [0]
try:
    auto = list(expense_sums['auto'].values) 
except KeyError: # no index
    auto = [0]
try:
    food = list(expense_sums['food'].values)
except KeyError: # no index
    food = [0]
try:
    entertainment = list(expense_sums['entertainment'].values)
except KeyError:
    entertainment = [0]
try:
    misc = list(expense_sums['miscellaneous'].values)
except KeyError:
    misc = [0]
try:
    gas = list(expense_sums['gas'].values)
except KeyError:
    gas = [0]
try:
    electric = list(expense_sums['electric'].values)
except KeyError:
    electric = [0]
try: 
    internet = list(expense_sums['internet'].values)
except KeyError:
    internet = [0]
try: 
    phone = list(expense_sums['phone'].values)
except KeyError:
    phone = [0]

print('{"income": {"x": ')
print(x)
print(', "y": ')
print(total_income)
print(', "type": "scatter", "name": "Total Income"}, "home": {"x": ')
print(x)
print(',"y": ')
print(home)
print(', "type": "scatter", "name": "Home"}, "auto": {"x": ')
print(x)
print(',"y": ')
print(auto)
print(', "type": "scatter", "name": "Auto"}, "food": {"x": ')
print(x)
print(',"y": ')
print(food)
print(', "type": "scatter", "name": "Food"}, "entertainment": {"x": ')
print(x)
print(',"y": ')
print(entertainment)
print(', "type": "scatter", "name": "Entertainment"}, "miscellaneous": {"x": ')
print(x)
print(',"y": ')
print(misc)
print(', "type": "scatter", "name": "Miscellaneous"}, "charity": {"x": ')
print(x)
print(',"y": ')
print(charity)
print(', "type": "scatter", "name": "Charity"}, "water": {"x": ')
print(x)
print(',"y": ')
print(water)
print(', "type": "scatter", "name": "Water"}, "gas": {"x": ')
print(x)
print(',"y": ')
print(gas)
print(', "type": "scatter", "name": "Gas"}, "electric": {"x": ')
print(x)
print(',"y": ')
print(electric)
print(', "type": "scatter", "name": "Electric"}, "internet": {"x": ')
print(x)
print(',"y": ')
print(internet)
print(', "type": "scatter", "name": "Internet"}, "phone": {"x": ')
print(x)
print(',"y": ')
print(phone)
print(', "type": "scatter", "name": "Phone"}}')
