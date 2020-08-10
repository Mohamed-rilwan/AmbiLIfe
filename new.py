# import openpyxl and tkinter modules 
from openpyxl import *
from tkinter import *
import pandas as pd
import datetime
import folium #for getting maps in pyton
from folium.map import *
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import FloatImage
import time
from geopy.distance import great_circle  # To calculate the GC distance
from model import TraficLight  # Import the MongoDB model
import time  # Required to use delay functions
import json
import paho.mqtt.publish as publish

root = Tk() 
root.geometry("300x300")
root.configure(background='deepsky blue') 
root.title("Location") 


mb = Menubutton(root, text= "Choose Ambulance Location")
mb.menu= Menu(mb)
mb["menu"]=mb.menu
mb.grid(row=4,column=1)
mb.menu.add_command(label ="Silkboard" , command=lambda: silkboard("Choosen location for demo is Silkboard Signal"))
mb.menu.add_command(label ="Marathahalli" , command=lambda: marathalli("Choosen location for demo is Marathalli Signal"))

mb.pack()


def silkboard(x):

        label = Label(root, text= x)    
        print (x)        
        # Broker running on local machine
        MQTT_BROKER = "13.233.84.7"
        signalA = [12.917200, 77.622379]
        signalB = [12.917324, 77.623191]
        signalC = [12.916822, 77.623019]

        #Ambulance GPS coordinates
        ambulance_loc = [(12.916469, 77.617765), (12.916401, 77.618291), (12.916432, 77.618870), (12.916639, 77.620321),
                        (12.916984, 77.621426), (12.917685, 77.623883), (12.916911, 77.628571)]

        # Ambulance location (GPS DATA) - for visual representation
        data = pd.DataFrame({
            'lon': [12.916469,12.916401,12.916432,12.916639,12.916984,12.917685,12.916911],
            'lat': [77.617765,77.618291,77.618870,77.620321,77.621426,77.623883,77.628571],
        })

        # Make an empty map
        m = folium.Map(location=signalA, tiles="CartoDBPositron", zoom_start=17)

        traffic_signals = []
        T = TraficLight.objects(places__match={"name": "Silkboard"})
        j = T.to_json()
        j_d = json.loads(j)

        for index,j in enumerate(ambulance_loc):

            for obj in j_d[-1]['places'][-1]['traffic_light_pos']:
                id = obj['_id']
                lon, lat = obj['location']['coordinates']
                traffic_signals.append((id, (lat, lon)))

            distances = []

            for i in traffic_signals:
                distances.append((i[0], great_circle(j, i[-1]).kilometers))

            print("Ambulance Distance from traffic signal A is", distances[0][-1])
            m = folium.Map(location=signalA, tiles="CartoDBPositron", zoom_start=17)
            folium.Marker([data.iloc[index]['lon'], data.iloc[index]['lat']], popup =("Ambulance live location"), tooltip= "Ambulance Live Location",
                        icon=folium.Icon(
                            icon_color='#FFFFFF',
                            icon="fa-ambulance", prefix='fa')).add_to(m)
            time.sleep(2)

            if distances[0][-1] > 0.4:
                publish.single(distances[0][0], payload="none", hostname=MQTT_BROKER, port=1883) #, client_id="AMB9632991318")
                folium.Marker(location=signalA, popup ="Silkboard traffic signal A",tooltip = "<strong> Silkboard traffic signal A</strong>", icon=folium.Icon(
                    icon_color='#FF0000',
                    icon="fa-circle", prefix='fa')).add_to(m)
                folium.Marker(location=signalB, popup ="Silkboard traffic signal B", tooltip = "Silkboard traffic signal B" , icon=folium.Icon(
                    icon_color='#00FF00',
                    icon="fa-circle", prefix='fa')).add_to(m)
                folium.Marker(location=signalC, popup ="Silkboard traffic signal C", tooltip = "Silkboard traffic signal C", icon=folium.Icon(
                    icon_color='#FF0000',
                    icon="fa-circle", prefix='fa')).add_to(m)
                m.save('index.html')

            elif distances[0][-1] > 0.2:
                publish.single(distances[0][0], payload="none", hostname=MQTT_BROKER,
                    port=1883)  # , client_id="AMB9632991318")
                folium.Marker(location=signalA, popup ="Silkboard traffic signal A", tooltip = "<strong> Silkboard traffic signal A </strong>", icon=folium.Icon(
                    icon_color='#FF0000',
                    icon="fa-circle", prefix='fa')).add_to(m)
                folium.Marker(location=signalB, popup ="Silkboard traffic signal B",tooltip = "Silkboard traffic signal B", icon=folium.Icon(
                    icon_color='#FF0000',
                    icon="fa-circle", prefix='fa')).add_to(m)
                folium.Marker(location=signalC, popup ="Silkboard traffic signal C", tooltip = "Silkboard traffic signal C" ,icon=folium.Icon(
                    icon_color='#00FF00',
                    icon="fa-circle", prefix='fa')).add_to(m)
                m.save('index.html')
            else:
                publish.single(distances[0][0], payload="open", hostname=MQTT_BROKER, port=1883) #, client_id="AMB9632991318")
                folium.Marker(location=signalA, popup ="Silkboard traffic signal A - [Ambulance has arrived]", tooltip ="<strong>Ambulance approching </strong>" ,icon=folium.Icon(
                    icon_color='#00FF00',
                    icon="fa-circle", prefix='fa')).add_to(m)
                folium.Marker(location=signalB, popup="Silkboard traffic signal B",tooltip = "Silkboard traffic signal B", icon=folium.Icon(
                    icon_color='#FF0000',
                    icon="fa-circle", prefix='fa')).add_to(m)
                folium.Marker(location=signalC, popup="Silkboard traffic signal C" , tooltip = "Silkboard traffic signal c", icon=folium.Icon(
                    icon_color='#FF0000',
                    icon="fa-circle", prefix='fa')).add_to(m)
                m.save('index.html')

        print("Saving the webpage for map....")
        print("done")
        label.pack()


root.mainloop() 
