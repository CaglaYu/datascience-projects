import pandas as pd
from sklearn.preprocessing import  LabelEncoder,OneHotEncoder
from sklearn.compose import ColumnTransformer

#form the dataframe from csv file
df=pd.read_csv("weather/pandas/1_intro/nyc_weather.csv")

#display EST of the records which have Rain as their event
print(   df.loc[df["Events"]=="Rain"]["EST"]    )

#Replace NaN's with 0's
df=df.fillna(0)

#display average humidity
print("{:.2f}".format(df["Humidity"].mean()))

#change dataset
df=pd.read_csv("weather/pandas/2_dataframe_basics/weather_data.csv")

#print(df[2:5]["event"])

dfc = pd.read_csv("1000_companies.csv")
#print(dfc.head)
X=dfc.iloc[:,:-1]
y=dfc.iloc[:,4]

X=dfc.iloc[:,:-1].values
y=dfc.iloc[:,4].values

lec=LabelEncoder()
X[:,3]=lec.fit_transform(X[:,3])
ct = ColumnTransformer([("State", OneHotEncoder(), [3])], remainder = 'passthrough')
X = ct.fit_transform(X)
print(X[:10])
X=X[:,1:]
print(X[:10])