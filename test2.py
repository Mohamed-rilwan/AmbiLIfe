import pandas as pd
import datetime
import folium
from folium.map import *
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import FloatImage
import time

SF_COORDINATES = (37.76, -122.45)

#m = folium.Map(location=SF_COORDINATES, zoom_start=13,tiles='CartoDBPositron')

ambulance_loc = [(12.916469, 77.617765), (12.916401, 77.618291), (12.916432, 77.618870), (12.916639, 77.620321),
                 (12.916984, 77.621426), (12.917685, 77.623883), (12.916911, 77.628571)]

# Make a data frame with dots to show on the map
data = pd.DataFrame({
'lat':[-58, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
'lon':[-34, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
'name':['Buenos Aires', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador']
})
data

# Make an empty map
m = folium.Map(location=[20, 0], tiles="CartoDBPositron", zoom_start=2)

# I can add marker one by one on the map
for i in range(0, len(data)):
    m = folium.Map(location=[20, 0], tiles="CartoDBPositron", zoom_start=2)
    folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name'], icon=folium.Icon(
        icon_color='#FFFFFF',
        icon='glyphicon glyphicon-plus')).add_to(m)
    time.sleep(2)
    print (data.iloc[i]['name'])
    m.save('index.html')

    """
# I can add marker one by one on the map
for i in range(0,len(data)):
    
    folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name'],icon=folium.Icon(
                             icon_color='#FFFFFF',
                             icon='glyphicon glyphicon-plus')).add_to(m)
    time.sleep(2)
    m.save('index.html')


"""
print ("Saving the webpage for map....")
