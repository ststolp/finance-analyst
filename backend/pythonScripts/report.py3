import sys  
import pandas as pd 
import numpy as np
from dateutil.parser import parse
from datetime import datetime
# startDate = sys.argv[1]
# endDate = sys.argv[2]
# now = sys.argv[3]
startDate = '2001-08-01'
endDate = '2005-12-31'
now = '2019-12-01'

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
datesColumn = generateDates(startDate, endDate)
# Get the dataFrame for actual income and expense transactions
expense_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/expense.csv')
income_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/income.csv')
expense_df['date'] = pd.to_datetime(expense_df['date'].values)
income_df['date'] = pd.to_datetime(income_df['date'].values)

# copy = expense_df['date'][0].strftime("%Y-%m")
# expense_df['date'][0] = copy
# print(expense_df['date'][0])

#print(expense_df)
# generate fabricated dataframe

expense_df_test = pd.DataFrame({'date': datesColumn, 'method': methodsColumn, 'category': catsColumn,
                               'amount': rng.integers(1, 500, size = num_fake_records)})
income_df_test = pd.DataFrame({'date': datesColumn, 'from': 'some guy', 'type': typesColumn,
                               'amount': rng.integers(1, 500, size = num_fake_records)})                               
# print(expense_df_test)
# print(income_df_test)
# print(expense_df_test)
# generate the stuff


x = list(range(0, expense_df['date'].size))

expense_sums = expense_df.pivot_table('amount', index='month', columns='category', aggfunc='sum', fill_value=0)
income_sums = income_df.pivot_table('amount', index='month', columns='type', aggfunc='sum', fill_value=0)
# expense_sums = expense_df_test.pivot_table('amount', index='month', columns='category', aggfunc='sum', fill_value=0)
# income_sums = income_df_test.pivot_table('amount', index='month', aggfunc='sum', fill_value=0)
# print(expense_sums)
# print(income_sums)

# TODO: only assign them stuff is there are values
total_income = list(income_sums.values)
home = list(expense_sums['home'].values)
auto = list(expense_sums['auto'].values)
food = list(expense_sums['food'].values)
entertainment = list(expense_sums['entertainment'].values)
misc = list(expense_sums['miscellaneous'].values)
charity = list(expense_sums['charity'].values)
water = list(expense_sums['water'].values)
gas = list(expense_sums['gas'].values)
electric = list(expense_sums['electric'].values)
internet = list(expense_sums['internet'].values)
phone = list(expense_sums['phone'].values)

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
print(', "type": "scatter", "name": "Phone"}}')
