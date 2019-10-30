import sys  
# TODO download pandas
import pandas as pd 
# index 0 is the filename
start_date = sys.argv[1]
# idea pass in the file name here!
end_date = sys.argv[2]
# Get the dataFrame for transactions
expense_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/expense.csv')
income_df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/income.csv')
print(expense_df)
print(income_df)
#beginning of python Script
#print(var1 + ', ' + var2 + ', ' + var3)