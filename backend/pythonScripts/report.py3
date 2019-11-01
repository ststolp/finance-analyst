import sys  
import pandas as pd 

startDate = sys.argv[1]
endDate = sys.argv[2]
now = sys.argv[3]
millisecondDay = 86400000

# Spread x values every 15 days
interval = millisecondDay * 15

# Get the dataFrame for income and expense transactions
expense_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/expense.csv')
income_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/income.csv')

# generate the stuff
# ....
# interval = 50
# startDate = 0
# endDate = 300
# now = 200
#x = list(range(startDate, endDate, interval))

# for testing purposes
x = [2015, 2016, 2017, 2018]
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
#print(x)
# lets pretend we have the stuff, for testing purposes
# return json object string
# '{"x": ' + x + ', "y": ' + incomeY + '...}
# outputa = '{"income": {"x": '
incomeY = [5000, 6000, 9000, 8000]
homeY = [800, 750, 1820, 930]
autoY = [300, 300, 600, 300]
print('{"income": {"x": ')
print(x)
print(', "y": ')
print(incomeY)
print(', "type": "scatter"}, "home": {"x": ')
print(x)
print(',"y": ')
print(homeY)
print(',"type": "scatter"}, "auto": {"x": ')
print(x)
print(',"y": ')
print(autoY)
print(', "type": "scatter"}}')
# + x + ', "y": [2000, 1000, 500, 1800], "type": "scatter"}, "home": {"x": ' + x + ',"y": [200, 100, 500, 1000],"type": "scatter"}, "auto":'
#outputb = '{"x": ' + x + ',"y": [600, 500, 450, 1000], "type": "scatter"}}'
#output = outputa + outputb
# print(output)