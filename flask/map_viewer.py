#!/usr/bin/python3
"""
Created Mar 17, 2021

Create map viewer using folium.
"""
import os
import json
import folium
from branca.element import Figure

path = os.getcwd()
param = 'ch4'

with open(path+'/data/stationsInfo.json','r') as f:
    stationsInfo = json.load(f)
with open(path+'/data/paramsInfo.json','r') as f:
    paramsInfo = json.load(f)[param]

#%%

points = [{
    'name': stationsInfo[ID]['name'],
    'coords' : (stationsInfo[ID]['lat'],stationsInfo[ID]['lon']),
    'country' : stationsInfo[ID]['country']
} for ID in stationsInfo.keys() & paramsInfo['stations']]

centroid = (52.23, 17.01)     # lat / lon

#%%
fig = Figure(width='80%', height='80%')

basemap = folium.Map(
    location        = centroid,
    control_scale   = True,
    zoom_start      = 5
)

fig.add_child(basemap)
folium.TileLayer('cartodbpositron').add_to(basemap)
folium.TileLayer('Stamen Toner').add_to(basemap)
folium.TileLayer('Stamen Terrain').add_to(basemap)

icosGroup = folium.FeatureGroup(name="ICOS").add_to(basemap)

for point in points:
    icon = folium.Icon(
        color       = 'white',
        icon        = 'train',
        icon_color  = 'red',
        prefix      = 'fa'          # font awesome lib
    )

    popup = folium.Popup(
        f"""station: {point['name']} <br>
        country: {point['country']} <br>""",
        max_width = len(f"station: {point['name']}") * 20)

    icosGroup.add_child(folium.Marker(
        point['coords'],
        icon    = icon,
        tooltip = 'Click here to see Popup',
        popup   = popup))


folium.LayerControl().add_to(basemap)
basemap.save(path+'/'+'map.html')
