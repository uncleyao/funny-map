import googlemaps
import csv
from datetime import datetime

# for directions
gmaps = googlemaps.Client(key='Your API key')

origins = []
destinations = []
f = open('place.csv')
csv_f = csv.reader(f)
for row in csv_f:
    print(row[0])
    origins.append(row[0])
    destinations.append(row[1])

now = datetime.now()
matrix = gmaps.distance_matrix(origins, destinations, language="en-AU",
                               avoid="tolls",
                               units="imperial",
                               departure_time=now,
                               traffic_model="optimistic")

distance_list = []
time_list = []
i = 0
while i < len(origins):
    distance_list.append(matrix['rows'][i]['elements'][i]['distance']['text'])
    time_list.append(matrix['rows'][i]['elements'][i]['duration']['text'])
    print(matrix['rows'][i]['elements'][i]['distance']['text'], matrix['rows'][i]['elements'][i]['duration']['text'])
    i = i + 1

rows = zip(distance_list,time_list)

resultFile = open("place.csv", 'w',newline='')
wr = csv.writer(resultFile, dialect='excel')
for row in rows:
    wr.writerow(row)

