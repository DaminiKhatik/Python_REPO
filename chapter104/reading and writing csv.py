
#Reading and Writing CSV 
import pandas as pd
df=pd.read_csv
mapReducedata = pd.read_csv(r'C:/Users/MyHP/Desktop/PYTHONbook/chapter104/mapReducedata.csv')
print(df)

#####writing csv in python
import pandas as pd
cities = pd.DataFrame([['Sacramento', 'California'], ['Miami', 'Florida']], columns=['City', 'State'])
cities.to_csv('cities.csv')

