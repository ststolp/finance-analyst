import sys  
# TODO download pandas
import pandas as pd 
# index 0 is the filename
# startDate = sys.argv[1]
# endDate = sys.argv[2]
# Get the dataFrame for transactions
df = pd.read_json('C:/Users/scsto/finance-analyst/backend/data/reportJson.json')

# generate the stuff
# ....
# lets pretend we have the stuff, for testing purposes
# return json object string
# TODO preserve double quotes
outputa = '{"income": {"x": [2015, 2016, 2017, 2018], "y": [2000, 1000, 500, 1800], "type": "scatter"}, "home": {"x": [2015, 2016, 2017, 2018],"y": [200, 100, 500, 1000],"type": "scatter"}, "auto":'
outputb = '{"x": [2015, 2016, 2017, 2018],"y": [600, 500, 450, 1000], "type": "scatter"}}'
output = outputa + outputb
print(output)