import sys  
import pandas as pd 
import numpy as np
from dateutil.parser import parse
from datetime import datetime

startDate = pd.to_datetime(sys.argv[1])
endDate = pd.to_datetime(sys.argv[2])
now = pd.to_datetime(sys.argv[3])
# startDate = pd.to_datetime('1/1/2019')
# endDate = pd.to_datetime('6/30/2019')
# now = pd.to_datetime('2/4/2019')

types = ['salary', 'bonus', 'commision', 'child support', 'interest']
categories =  ['home', 'auto', 'food', 'entertainment', 'phone', 'internet', 'water', 'gas', 'charity',
'electric', 'miscellaneous', 'income']
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

# expense_df_test = pd.DataFrame({'date': datesColumn, 'method': methodsColumn, 'category': catsColumn,
#                                'amount': rng.integers(1, 500, size = num_fake_records)})

expense_sums = new_expense.pivot_table('amount', index='month', columns='category', aggfunc='sum', fill_value=0)

x = list(range(len(expense_sums.index)))
# expense_sums = expense_df_test.pivot_table('amount', index='month', columns='category', aggfunc='sum', fill_value=0)
# income_sums = income_df_test.pivot_table('amount', index='month', aggfunc='sum', fill_value=0)

# TODO: The number of zeros have to match the length of indexes
zeroList = []
for b in x:
    zeroList.append(0)

for category in categories:
    try: 
        list(expense_sums[category].values)
    except KeyError:
        expense_sums[category] = zeroList

# TODO: If now comes before the endDate, Only predict one month in the future based on 
# the trajectory from the last two data samples.
# "Always in motion is the future - Yoda"
# Use dataframe append function
if now < endDate:
    # add one month to the time axis
    x.append(len(x))
    # iterate through all of the columns like categories, 
    future_df = pd.DataFrame()
    future_df['date'] = 'future'
    future_df.index = future_df['date']
    for category in categories:
        if len(expense_sums[category]) < 2:
            future_df[category] = [expense_sums[category][0]]
        else:
            future_df[category] = [expense_sums[category][len(expense_sums[category]) - 1] + expense_sums[category][len(expense_sums[category]) - 1] - expense_sums[category][len(expense_sums[category]) - 2]]
    expense_sums = expense_sums.append(future_df)

print('{"income": {"x": ')
print(x)
print(', "y": ')
print(list(expense_sums['income'].values))
print(', "type": "scatter", "name": "Total Income"}, "home": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['home'].values))
print(', "type": "scatter", "name": "Home"}, "auto": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['auto'].values))
print(', "type": "scatter", "name": "Auto"}, "food": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['food'].values))
print(', "type": "scatter", "name": "Food"}, "entertainment": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['entertainment'].values))
print(', "type": "scatter", "name": "Entertainment"}, "miscellaneous": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['miscellaneous'].values))
print(', "type": "scatter", "name": "Miscellaneous"}, "charity": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['charity'].values))
print(', "type": "scatter", "name": "Charity"}, "water": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['water'].values))
print(', "type": "scatter", "name": "Water"}, "gas": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['gas'].values))
print(', "type": "scatter", "name": "Gas"}, "electric": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['electric'].values))
print(', "type": "scatter", "name": "Electric"}, "internet": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['internet'].values))
print(', "type": "scatter", "name": "Internet"}, "phone": {"x": ')
print(x)
print(',"y": ')
print(list(expense_sums['phone'].values))
print(', "type": "scatter", "name": "Phone"}}')
