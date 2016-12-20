__author__ = 'yyao'

import googlemaps
import csv
import datetime
import time

# for directions

gmaps3 = googlemaps.Client(key='your key')

origins = []
destinations = ['221 Shepard St, Ripon, WI 54971']
f = open('separations.csv')
csv_f = csv.reader(f)
for row in csv_f:
    #print(row[0])
    origins.append(row[0])

now = datetime.datetime(2016,11,9)
print(now)

distance_list = []
time_list = []
i = 0

resultFile = open("outputactive501-800.csv", 'a',newline='')
wr = csv.writer(resultFile, dialect='excel')
print('heheheheeheheheeheh')
while i < len(origins):
    filed = []
    origins_one = []
    origins_one.append(origins[i])
    print(origins_one)
    if i % 2 == 0:
        matrix = gmaps3.distance_matrix(origins_one, destinations, language="en-AU",
                                   avoid="tolls",
                                   units="imperial",
                                   departure_time=now,
                                   traffic_model="optimistic")
        print(matrix)
        print(i+1,origins[i],matrix['rows'][0]['elements'][0]['distance']['text'], matrix['rows'][0]['elements'][0]['duration']['text'])
        filed = [origins[i],matrix['rows'][0]['elements'][0]['distance']['text'], matrix['rows'][0]['elements'][0]['duration']['text']]
        wr.writerow(filed)
    else:
        matrix = gmaps3.distance_matrix(origins_one, destinations, language="en-AU",
                                   avoid="tolls",
                                   units="imperial",
                                   departure_time=now,
                                   traffic_model="optimistic")
        print(i+1,origins[i],matrix['rows'][0]['elements'][0]['distance']['text'], matrix['rows'][0]['elements'][0]['duration']['text'])
        filed = [origins[i],matrix['rows'][0]['elements'][0]['distance']['text'], matrix['rows'][0]['elements'][0]['duration']['text']]
        wr.writerow(filed)
    time.sleep(10)
    i = i +1
