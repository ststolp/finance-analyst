import sys  
# TODO download pandas
import pandas as pd 
# index 0 is the filename
var1 = sys.argv[1]
# idea pass in the file name here!
var2 = sys.argv[2]
var3 = sys.argv[3]
# Get the dataFrame for transactions
if (var1 == 'read'):
   df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/transactions.csv')
   df.to_json(orient='records')
   print(df)
#beginning of python Script
#print(var1 + ', ' + var2 + ', ' + var3)