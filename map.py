import folium
import pandas as p

data = p.read_csv("world2.csv")
lat = list(data["latitude"])
lon = list(data["longitude"])
coun = list(data["country"])

map = folium.Map(location=[13.103,80.273])

fg = folium.FeatureGroup(name="MAP")
i = 0
for lt,ln in zip(lat,lon):
    try:
        fg.add_child(folium.CircleMarker(location=[lt,ln],popup=coun[i], radius=6, fill="true", fill_color="grey",
        color = "green", fill_opacity = 0.76))
        
        i+=1
    except:
        continue

map.add_child(fg)
map.save("maps.html")
