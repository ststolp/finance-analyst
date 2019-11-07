import sys  
import pandas as pd 
import numpy as np
startDate = sys.argv[1]
endDate = sys.argv[2]
now = sys.argv[3]
millisecondDay = 86400000

# Spread x values every 15 days
interval = millisecondDay * 15
types = ['salary', 'bonus', 'commision', 'child support', 'interest']
cats =  ['home', 'auto', 'food', 'entertainment', 'phone', 'internet', 'water', 'gas', 'charity',
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

methodsColumn = generateColumn(methods, num_fake_records)
typesColumn = generateColumn(types, num_fake_records)
catsColumn = generateColumn(cats, num_fake_records)

# Get the dataFrame for actual income and expense transactions
expense_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/expense.csv')
income_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/income.csv')
# print(expense_df)
# print(income_df)

# generate fabricated dataframe

# TODO: fabricate the Dates, don't bother with payment_to or description
# expense_df_test = pd.DataFrame({'date': ?, 'method': methodsColumn, 'category': catsColumn,
#                                'amount': rng.integers(1, 500, size = num_fake_records)})

# print(expense_df_test)
# generate the stuff
# ....
# interval = 50
# startDate = 0
# endDate = 300
# now = 200
#x = list(range(startDate, endDate, interval))

incomeY = []
homeY = []
autoY = []
foodY = []
entertainmentY = []
miscY = []
charityY = []
waterY = []
gasY = []
electricY = []
internet = []
phoneY = []
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

incomeY = [5000, 6000, 9000, 8000]
homeY = [800, 750, 1820, 930]
autoY = [300, 300, 600, 300]
print('{"income": {"x": ')
print(x)
print(', "y": ')
print(incomeY)
print(', "type": "scatter", "name": "Income"}, "home": {"x": ')
print(x)
print(',"y": ')
print(homeY)
print(', "type": "scatter", "name": "Home"}, "auto": {"x": ')
print(x)
print(',"y": ')
print(autoY)
print(', "type": "scatter", "name": "Auto"}}')
