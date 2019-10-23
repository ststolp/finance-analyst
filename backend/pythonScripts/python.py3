import sys  
# TODO download pandas
import pandas as pd 
# index 0 is the filename
#var1 = sys.argv[1]
#var2 = sys.argv[2]
#var3 = sys.argv[3]
var1 = 'read'
# Get the dataFrame for transactions
if (var1 == 'read'):
   df = pd.read_csv('C:/Users/scsto/finance-analyst/backend/data/transactions.csv')
   print(df)
#beginning of python Script
#print(var1 + ', ' + var2 + ', ' + var3)