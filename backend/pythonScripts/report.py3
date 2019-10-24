import sys  
# TODO download pandas
import pandas as pd 
# index 0 is the filename
#var1 = sys.argv[1]
#var2 = sys.argv[2]
#var3 = sys.argv[3]
# Get the dataFrame for transactions
df = pd.read_json('C:/Users/scsto/finance-analyst/backend/data/reportJson.json')

# generate the stuff
# ....
# lets pretend we have the stuff, for testing purposes
# return json object string
# TODO preserve double quotes
print({"income": 
    {
     "x": [2015, 2016, 2017, 2018], 
     "y": [2000, 1000, 500, 1800], 
     "type": "scatter"
    }, 
"home": 
    {
      "x": [2015, 2016, 2017, 2018],
      "y": [200, 100, 500, 1000],
      "type": "scatter"
    }, 
"auto": 
    {
      "x": [2015, 2016, 2017, 2018],
      "y": [600, 500, 450, 1000], 
      "type": "scatter"
    }
})