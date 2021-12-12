import pandas as pd

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

print(df[2:5]["event"])

dfc = pd.read_csv("1000_companies.csv")
print(dfc.head)




