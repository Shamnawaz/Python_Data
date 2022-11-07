import pandas as pd
import matplotlib.pyplot as plt
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
flights_data.rename(columns={'name': 'airline_name'}, inplace=True)
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
# Question 1.1.a :
question11a = len(airport_data['faa'].unique())
question11b = len(flights_data['origin'].unique())
question11c = len(flights_data['dest'].unique())
question12a = airport_data['dst'].value_counts()['N']
question12b = len(airport_data['tzone'].unique())
question13a = len(airlines_data)
question13b = len(planes_data['tailnum'].unique())
question13c = flights_data['air_time'].value_counts()[0]
# print(len(airport_data['faa'].unique()))
# print(len(flights_data['origin'].unique()))
# print(len(flights_data['dest'].unique()))
# Question 1.1.b : 
# print(airport_data['dst'].value_counts()['N'])
# print(len(airport_data['tzone'].unique()))
# Question 1.1.c : 
# print(len(airlines_data))
# print(len(planes_data['tailnum'].unique()))
# print(flights_data['air_time'].value_counts()[0])
# Désactivez le drop des cellules vides ou NaN : print(flights_data['air_time'].value_counts(dropna=False))
#                       question 2
dest_plus_moins =airport_flights.groupby('name')['year'].count().reset_index(name='nb_vols').sort_values(['nb_vols'],ascending=False)
dest_plus_moins['pourcentage']=((dest_plus_moins['nb_vols']/len(airport_flights))*100)
question2a = flights_data.groupby('origin').count().head(1)
question2b1 =dest_plus_moins.head(10)
question2b2 =dest_plus_moins.tail(10)
# data = flights_data.dest.value_counts().reset_index().rename(columns = {'index':'faa', 'dest':'nb_vols'},inplace=True).merge(airlines_data, how='inner', on='faa')[['name','nb_vols']]
# data['percent']=(data['nb_vols']/data['nb_vols'].sum())*100
# print(data)
# print(flights_data[flights_data['air_time'].ne(" ")].groupby('tailnum')['year'].count().reset_index(name='nb_decollage').sort_values(['nb_decollage'],ascending=False).head(10))
# print(flights_data[flights_data['air_time'].ne(" ")].groupby('tailnum')['year'].count().reset_index(name='nb').sort_values(['nb'],ascending=False).tail(10))
# print("'''''''''''''''''''''''''''''''''''''''''''''''")
# print(flights_data.groupby('tailnum').min().sort_values(ascending=False))
question2c1 = flights_data[flights_data['air_time'].ne(" ")].groupby('tailnum')['year'].count().reset_index(name='nb_decollage').sort_values(['nb_decollage'],ascending=False).head(10)
question2c2 = flights_data[flights_data['air_time'].ne(" ")].groupby('tailnum')['year'].count().reset_index(name='nb_decollage').sort_values(['nb_decollage'],ascending=False).tail(10)
#                                           Question 3
# print(flights_data.groupby(['carrier'])['dest'].count())
# print(flights_data.groupby(['carrier','origin'])['dest'].count())
question3a= pd.DataFrame(flights_data[flights_data['air_time'].ne(" ")].groupby(['carrier','dest'])['dest'].count())
question3b = pd.DataFrame(flights_data[flights_data['air_time'].ne(" ")].groupby(['carrier','origin'])['dest'].count())
question3a.plot.bar(ylabel='nb_vols', xlabel='airlines').set_title('Question 3a')
question3b.plot.bar(ylabel='nb_vols', xlabel='airlines').set_title('Question 3b')
# plt.show()
#                                           Question 4
id_seattle = airport_data['faa'][airport_data['name'].eq('Seattle Tacoma Intl')]
question4a = flights_data[flights_data['dest'].eq('IAH') | flights_data['dest'].eq('HOU')]
question4b = len(flights_data[flights_data['dest'].eq(id_seattle.values[0])])
question4c = len(flights_data.carrier[flights_data['dest'].eq(id_seattle.values[0])].unique())
question4d = len(flights_data.tailnum[flights_data['dest'].eq(id_seattle.values[0])].unique())
# print(flights_data[flights_data['dest'].eq('IAH') | flights_data['dest'].eq('HOU')])
# print(flights_data['dest'].value_counts()['IAH' and 'HOU'])
# print(len(flights_data[flights_data['dest'].eq(id_seattle.values[0])]))
# print(len(flights_data.carrier[flights_data['dest'].eq(id_seattle.values[0])].unique()))
# print(len(flights_data.tailnum[flights_data['dest'].eq(id_seattle.values[0])].unique()))
#                                           Question 5
question5a = flights_data.groupby('dest')['year'].count().reset_index(name='nb_vols').sort_values(['nb_vols'],ascending=False)
question5b = airport_flights_airlines.groupby(['dest','name', 'airport_name'])['year'].count().reset_index(name='nb_vols').sort_values(['nb_vols'])
# print(flights_data.groupby('dest')['year'].count().reset_index(name='nb_vols').sort_values(['nb_vols'],ascending=False))
# print(airport_flights_airlines.groupby(['dest','name', 'airport_name'])['year'].count().reset_index(name='nb_vols').sort_values(['nb_vols']))
#                                           Question 6
# print(flights_airlines.name.value_counts())
a = flights_data.groupby(['carrier','origin']).size().reset_index().groupby('carrier').size()
b =flights_data.groupby(['carrier','dest']).size().reset_index().groupby('carrier').size().sort_values(ascending=False)
# print(flights_airlines.name[flights_airlines['origin'].eq(None)].count())
# # print(a.where((a != 3)).sort_values(ascending=False).dropna())
# # print(b.where((b == len(flights_airlines.name))).sort_values(ascending=False).dropna())
question6a = len(a.where((a != 3)).sort_values(ascending=False).dropna())
question6b = len(b.where((b == len(flights_airlines.name))).sort_values(ascending=False).dropna())
# print(question6a)
# print(question6b)
#                                           Question 7
y =  pd.DataFrame(flights_data.groupby('dest')['carrier'].unique())
z = pd.DataFrame(flights_data.groupby(['dest','carrier'])['dest'].unique())
# aa = flights_data['dest'].where(len(flights_data['carrier']) == 1)
x=0
print(y)
question7 = pd.DataFrame
# while x < len(y) : 
#     if len(y.values[x]) == 1 :
        # print(y.values[x])
        # question7 = pd.concat(question7,y.values[x])
    # x+=1
# print(z.where(len(z['carrier'])==1))
# print(z.columns)
# print(y)
# print(z)
# print(z.values[0])
# print(question7)
#                                           Question 8
exploit = pd.merge(flights_data, airlines_data, how='inner', on="carrier")
listin = ['American Airlines Inc.','Delta Air Lines Inc.','United Air Lines Inc.']
# print(question8[question8['name'].isin(listin)])
question8 = exploit[exploit['name'].isin(listin)]
print(
'''
PROJET FLIGHTS
Mission 1 :
Question 1 : 
1.a.1-Nombre d'aéoroport en tout : {}  
1.a.2-Nombre de départ : {}
1.a.3-Nombre de destination : {}
1.b.1-Nombre d'aéroport aux USA sans changement d'heure : {} 
1.b.2-Nombre de fuseaux horaires : {}
1.c.1-Nombre de compagnies : {} 
1.c.2-Nombre d'avions : {} 
1.c.3-Nombre de vols annulés : {}
Question 2 :
2.a-Aéroport le plus emprunté : {}
2.b.1-Top 10 destinations les plus prisées :
{}
2.b.2-Bottom 10 destinations les moins prisées :
{}
2.c.1-Top 10 avions ayant le plus décollé
{}
2.c.2-Top 10 avions ayant le moins décollé
{}
Question 3 :
3.a-Nombre de destinations desservie par compagnie (cf graph1):
{}
3.b-Nombre de destinations deservie par compagnie par aéroport d'origine (cf graph2):
{}
Question 4 :
4.a-Vols ayant atteri à Houston :
{}
4.b-Nombre de vols partant de NYC pour Seattle :
{}
4.c-Nombre de compagnies pour Seattle :
{}
4.d-Nombre d'avions unique :
{}
Question 5 :
5.a-Nombre de vols par destination :
{}
5.b- Tri suivant la destination, l'aéroport d'origine et la compagnie par ordre croissant : 
{}
Question 6 :
6.a-Nombre de compagnies qui n'opèrent pas sur tout les aéroports d'origines : 
{}
6.b-Nombre de compagnies qui déservent toutes les destinations : 
{}
Question 7 :
7-Destinations exclusives à certaines compagnies :
{}
Question 8 :
8-Vols exploités par United, American ou Delta :
{}
'''.format(question11a,
           question11b,
           question11c,
           question12a,
           question12b,
           question13a,
           question13b,
           question13c,
           question2a,
           question2b1,
           question2b2,
           question2c1,
           question2c2,
           question3a,
           question3b,
           question4a,
           question4b,
           question4c,
           question4d,
           question5a,
           question5b,
           question6a,
           question6b,
           question7,
           question8))