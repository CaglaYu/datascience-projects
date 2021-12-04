import pandas as pd

#form the dataframe fromcsv file with setting the first two rows as header
Data_Set1=pd.read_csv("Data_Set.csv",header=2)

#form the dataframe from csv file
Data_Set2=pd.read_csv("Data_Set.csv")

#change column name
Data_Set3=Data_Set1.rename(columns={"Temperature":"Temp"})

#drop a column
Data_Set4=Data_Set3.drop('No. Occupants',axis=1)

#drop a row based on its index
Data_Set4=Data_Set4.drop(2)
Data_Set4=Data_Set4.reset_index(drop=True)

myval=Data_Set4.index[Data_Set4["E_Heat"]==Data_Set4["E_Heat"].min() ].tolist()[0]
#print(Data_Set4.head(6))
#Data_Set4.loc[((Data_Set4["Price"]=="10") and (Data_Set4["E_Plug"]>16)),"Price"]="33"

#change column values based on their value
Data_Set4.loc[Data_Set4["E_Heat"]==-4,"E_Heat"]=21
print(Data_Set4.head(46))




