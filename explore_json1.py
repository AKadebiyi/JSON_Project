import json

infile = open('eq_data_1_day_m1.json', 'r')
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)
#the load function converts the data into a format Python understands, a giant dictionary

json.dump(eq_data, outfile, indent=5) #just for viewing better
#actual obj is eq_data

print(type(eq_data))

list_of_eqs = eq_data['features']

print(len(list_of_eqs))


mags,lats,lons = [],[],[]

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    lat = eq['geometry']['coordinates'][1]
    lon = eq['geometry']['coordinates'][0]

    mags.append(mag)
    lats.append(lat)
    lons.append(lon)

print(mags[:10]) #to print first 10 values of each list
print(lats[:10])
print(lons[:10])

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

my_data = Scattergeo(lon=lons,lat=lats) #world map

my_layout = Layout(title="Global Earthquakes")

fig = {'data':my_data,'layout':my_layout}

offline.plot(fig,filename='global_earthquakes.html')
