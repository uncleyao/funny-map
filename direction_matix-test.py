import googlemaps
import csv
from datetime import datetime

# for directions
##gmaps = googlemaps.Client(key='AIzaSyDbM-SN7CD6Q60g3LjApyZOcfGujJEpDJg')
gmaps = googlemaps.Client(key='AIzaSyCOVf2O56NW1LAX8xrqXPmZcYr206lUa7I')
origins = []
destinations = ['221 Shepard St, Ripon, WI 54971']
f = open('active.csv')
csv_f = csv.reader(f)
for row in csv_f:
    print(row[0])
    origins.append(row[0])

now = datetime.now()

distance_list = []
time_list = []
i = 0

print('heheheheeheheheeheh')
while i < len(origins):
    origins_one = []
    origins_one.append(origins[i])
    matrix = gmaps.distance_matrix(origins_one, destinations, language="en-AU",
                                   avoid="tolls",
                                   units="imperial",
                                   departure_time=now,
                                   traffic_model="optimistic")
    distance_list.append(matrix['rows'][0]['elements'][0]['distance']['text'])
    time_list.append(matrix['rows'][0]['elements'][0]['duration']['text'])
    print(matrix['rows'][0]['elements'][0]['distance']['text'], matrix['rows'][0]['elements'][0]['duration']['text'])
    i = i + 1

rows = zip(distance_list,time_list)

resultFile = open("output7.csv", 'w',newline='')
wr = csv.writer(resultFile, dialect='excel')
for row in rows:
    wr.writerow(row)



