import json

infile = open('eq_data_30_day_m1.json', 'r')#switch to 30 days
outfile = open('readable_eq_data.json', 'w')

eq_data = json.load(infile)
#the load function converts the data into a format Python understands, a giant dictionary

json.dump(eq_data, outfile, indent=5) #just for viewing better
#actual obj is eq_data

print(type(eq_data))

list_of_eqs = eq_data['features']

print(len(list_of_eqs))


mags,lats,lons,hover_texts = [],[],[],[]

for eq in list_of_eqs:
    mag = eq['properties']['mag']
    if mag > 5:
        lat = eq['geometry']['coordinates'][1]
        lon = eq['geometry']['coordinates'][0]
        title = eq['properties']['title']

        mags.append(mag)
        lats.append(lat)
        lons.append(lon)
        hover_texts.append(title)

print(mags[:10]) #to print first 10 values of each list
print(lats[:10])
print(lons[:10])

from plotly.graph_objs import Scattergeo,Layout
from plotly import offline

#my_data = Scattergeo(lon=lons,lat=lats) #world map #doesn't allow for customization
my_data = [{'type':'scattergeo','lon':lons,'lat':lats,'text':hover_texts,
            'marker':{'size':[5 * mag for mag in mags],
                      'color':mags,'colorscale':'Viridis','reversescale':True,
                      'colorbar':{'title':'Magnitude'}}}]

my_layout = Layout(title="Global Earthquakes")

fig = {'data':my_data,'layout':my_layout}

offline.plot(fig,filename='global_earthquakes.html')
