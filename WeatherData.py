import pandas as pd

#form the dataframe from csv file
df=pd.read_csv("weather/pandas/1_intro/nyc_weather.csv")
print(   df.loc[df["Events"]=="Rain"]["EST"]    )





