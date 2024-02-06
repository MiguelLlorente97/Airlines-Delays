#Importing Libreries To Use

import pandas as pd

import matplotlib.pyplot as plt

#Importing dataset

df = pd.read_csv('C:/Users/Miguel.Llorente/OneDrive - FleetCor/Desktop/Airlines Delay/airline_delay.csv')
df.head(20)
df.info()
df.describe()
print(df)
#Data Warling
#Changing the NaN to the average value of the colum
mean_value = df['carrier_delay'].mean()
df['carrier_delay'] = df['carrier_delay'].fillna(mean_value)    

new_df = df.dropna()
print(new_df)

df = df.fillna(mean_value)

#Wich airline has more delays

column_elimante = ['weather_delay','security_delay', 'late_aircraft_delay','arr_delay' ]##Chossing columns i want to delate
filter_df = df.drop(column_elimante,axis=1)#delating the column ina  new DF
filter_df.head()
delay_airline = df['carrier_name']


#summing the delay that is not ocasionate by the airline as the security or the wheather
df['no_airline_fault'] = df['weather_delay'] + df['security_delay'] + df['nas_delay']
df['airline_delay'] = df['arr_delay'] - df['no_airline_fault']#creating a culum with the delate time that is ocasinate for the airline


delay_airline_fault =  ['carrier','carrier_name','airport','airline_delay' ]# creating a new df just with the column i want to anilize in this case
delay_df = df[delay_airline_fault]
print(delay_df)


##Filtering the data to see witch airline have more minutes of delay
delay_airlines = delay_df.groupby('carrier_name')['airline_delay'].sum()
airline_max_delay = delay_airlines.idxmax()
print(airline_max_delay)
df_sorted = delay_airlines.sort_values(ascending=True)
print(df_sorted)

df_sorted.sort_values('airline_delay')

df_sorted = delay_airlines.sort_values(ascending=False)##Airlines with most delay
print(df_sorted)

##checking with airport has the most delays

airport_delay = delay_df.groupby('airport')['airline_delay'].sum()
airport_delay1 = airport_delay.sort_values(ascending=False)
print(airport_delay1) #Airport with more delays in america are DFW, ORD, DEN,ATL, and  with less RIW,BFM,PGV


df['RefNumber'] = df.reset_index().index
print(df)

##checking airport with more weather delays
#
weather_delays = df.groupby('airport')['weather_delay'].sum()##Code suming the weather delay and filtering by the airport code.
print(weather_delays)


weather_delays_sort = weather_delays.sort_values(ascending= False)
print(weather_delays_sort)## airport with most delay by the weather are MSP, DFW, ORD, DTW


##checking months with more delays by the weather.

month_weather_delay = df.groupby('month')['weather_delay'].sum()
print(month_weather_delay)##Month with more delay by the weather is December

## aiport with more delays by security 

security_delay = df.groupby('airport')['security_delay'].sum()
security_delay_sort = security_delay.sort_values(ascending = False)
print(security_delay_sort)## Airport with most security delays are PNS, BDS, STL, CHA, FAI


