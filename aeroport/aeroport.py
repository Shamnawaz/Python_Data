import pandas as pd

airport_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/airports.csv"
airline_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/airlines.csv"
flights_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/flights.csv"
planes_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/planes.csv"
weather_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/weather.csv"


airport_data = pd.read_csv(airport_path,index_col='name')
airlines_data =pd.read_csv(airline_path)
flights_data =pd.read_csv(flights_path)
planes_data =pd.read_csv(planes_path)
weather_data =pd.read_csv(weather_path)

# Question 1.1.a : print(len(airport_data['faa'].unique()))
# print(len(flights_data['origin'].unique()))
# print(len(flights_data['dest'].unique()))
# Question 1.1.b : print(airport_data['dst'].value_counts()['N'])
#print(len(airport_data['tzone'].unique()))
# Question 1.1.c : print(len(airlines_data))
# print(len(planes_data['tailnum'].unique()))
# print(flights_data['air_time'].value_counts()[0])
# Désactivez le drop des cellules vides ou NaN : print(flights_data['air_time'].value_counts(dropna=False))
# print (flights_data.groupby('origin').count())
# print(flights_data.groupby('origin').count().head(1))
# print(flights_data.groupby('dest').count().head(10))
# print(flights_data.groupby('dest').count().tail(10))
