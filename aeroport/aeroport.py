import pandas as pd
# import matplotlib as mp

#https://stackoverflow.com/questions/20333435/pandas-comparison-raises-typeerror-cannot-compare-a-dtyped-float64-array-with
#https://www.analyticsvidhya.com/blog/2021/06/join-the-dataframes-like-sql-tables-in-python-using-pandas/

airport_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/airports.csv"
airline_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/airlines.csv"
flights_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/flights.csv"
planes_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/planes.csv"
weather_path= "D:/IPSSI M1/Python Data/aeroport/aeroport/donnees/weather.csv"



airport_data = pd.read_csv(airport_path)
airlines_data =pd.read_csv(airline_path)
flights_data = pd.read_csv(flights_path)
planes_data = pd.read_csv(planes_path)
weather_data = pd.read_csv(weather_path)

airport_flights = pd.merge(flights_data,airport_data,how = "inner", left_on = 'dest', right_on = 'faa')
flights_airlines = pd.merge(flights_data,airlines_data,how='inner',left_on='carrier',right_on='carrier')
# print(flights_airlines)
airport_flights_2 = pd.merge(flights_data,airport_data, how = "inner", left_on = 'origin', right_on = 'faa')
# print(airport_flights_2.columns)
# print(airlines_data.columns)
airport_flights_2.rename(columns={'name': 'airport_name'}, inplace=True)
# print(airport_flights_2.columns)
airport_flights_airlines = pd.merge(airport_flights_2, airlines_data, how = "outer", left_on='carrier', right_on='carrier')
# print(airport_flights_airlines.columns)

# Question 1.1.a : print(len(airport_data['faa'].unique()))
# print(len(flights_data['origin'].unique()))
# print(len(flights_data['dest'].unique()))
# Question 1.1.b : print(airport_data['dst'].value_counts()['N'])
# print(len(airport_data['tzone'].unique()))
# Question 1.1.c : print(len(airlines_data))
# print(len(planes_data['tailnum'].unique()))
# print(flights_data['air_time'].value_counts()[0])
# Désactivez le drop des cellules vides ou NaN : print(flights_data['air_time'].value_counts(dropna=False))
# print (flights_data.groupby('origin').count())
# print(flights_data.groupby('origin').count().head(1))
 # dest_plus =airport_flights.groupby('name')['year'].count().reset_index(name='nb_vols').sort_values(['nb_vols'],ascending=False).head(10)
# dest_moins =airport_flights.groupby('name')['year'].count().reset_index(name='nb_vols').sort_values(['nb_vols'],ascending=False).tail(10)
# dest_plus['percent']=((dest_plus['nb_vols']/len(airport_flights))*100)
# print('10 dest + prisé')
# print(dest_plus)
# dest_moins['percent']=((dest_moins['nb_vols']/len(airport_flights))*100)
# print('10 dest - prisé')
# print(dest_moins)

# data = flights_data.dest.value_counts().reset_index().rename(columns = {'index':'faa', 'dest':'nb_vols'},inplace=True).merge(airlines_data, how='inner', on='faa')[['name','nb_vols']]
# data['percent']=(data['nb_vols']/data['nb_vols'].sum())*100
# print(data)

# print(flights_data[flights_data['air_time'].ne(" ")].groupby('tailnum')['year'].count().reset_index(name='nb').sort_values(['nb'],ascending=False).head(10))
# print(flights_data[flights_data['air_time'].ne(" ")].groupby('tailnum')['year'].count().reset_index(name='nb').sort_values(['nb'],ascending=False).tail(10))
# # print("'''''''''''''''''''''''''''''''''''''''''''''''")
# print(flights_data.groupby('tailnum').min().sort_values(ascending=False))
#                                           Question 3
print(flights_data.groupby(['carrier'])['dest'].count())
print(flights_data.groupby(['carrier','origin'])['dest'].count())
#                                           Question 4
#   
# print(flights_data[flights_data['dest'].eq('IAH') | flights_data['dest'].eq('HOU')])
# print(flights_data['dest'].value_counts()['IAH' and 'HOU'])
# id_seattle = airport_data['faa'][airport_data['name'].eq('Seattle Tacoma Intl')]
# print(len(flights_data[flights_data['dest'].eq(id_seattle.values[0])]))
# print(len(flights_data.carrier[flights_data['dest'].eq(id_seattle.values[0])].unique()))
# print(len(flights_data.tailnum[flights_data['dest'].eq(id_seattle.values[0])].unique()))

#                                           Question 5

# print(flights_data.groupby('dest')['year'].count().reset_index(name='nb_vols').sort_values(['nb_vols'],ascending=False))
# print(airport_flights_airlines.groupby(['dest','name', 'airport_name'])['year'].count().reset_index(name='nb_vols').sort_values(['nb_vols']))


#                                           Question 6
# print(flights_airlines.name.value_counts())

# print(flights_airlines.name[flights_airlines['origin'].eq(None)].count())
# a = flights_data.groupby(['carrier','origin']).size().reset_index().groupby('carrier').size()
# print(len(a.where((a != 3)).sort_values(ascending=False).dropna()))
# b =flights_data.groupby(['carrier','dest']).size().reset_index().groupby('carrier').size().sort_values(ascending=False)

# print(len(b.where((b == len(flights_airlines.name))).sort_values(ascending=False).dropna()))


#                                           Question 7

#                                           Question 8

# df_merged = pd.merge(flights_data, airlines_data, how='inner', on="carrier")
# listin = ['American Airlines Inc.','Delta Air Lines Inc.','United Air Lines Inc.']
# print(df_merged[df_merged['name'].isin(listin)])
