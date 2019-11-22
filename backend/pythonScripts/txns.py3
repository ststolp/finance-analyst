import sys  
# TODO download pandas
import pandas as pd 
from datetime import datetime
# index 0 is the filename
#start_date = sys.argv[1]
# idea pass in the file name here!
#end_date = sys.argv[2]
# Get the dataFrame for transactions
# expense_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/expense.csv')
# income_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/income.csv')
list_a = [1, 2, 3 ,4 ]
string = '2019-19-15'
state = string[0:7] 
now = datetime.now()
date = now.strftime("%Y-%m")
print(date)
# print(expense_df)
# print(income_df)
#beginning of python Script
#print(var1 + ', ' + var2 + ', ' + var3)