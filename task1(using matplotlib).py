#import requests,json and matplotlib

import requests
import json
import matplotlib.pyplot as plt
import key  #import the API_KEY from the key file

#enter city name from the user

CITY_NAME=input("enter the city name :")

 #import the API_KEY from the key

#select API from openweathermap.org and click built-on API request by city name and select the URL

URL=f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={key.API_KEY}&units=metric"
a=requests.get(URL)
data=a.json()
#print(data)

#extract temperature and time

temperature=[]
time=[]

#add the temperature and time from the taken city in the openweathermap.org

temperature.append(data['main']['temp'])
print(f"Current Temperature : {temperature}")
time.append(data["timezone"])
print(f"Current Time : {time}")

#addig color,size and family to the text

f1={'family':'arial','color':'c','size':20}
f2={'family':'arial','color':'b','size':20}
f3={'family':'arial','color':'b','size':20}


print(plt.figure(figsize=(10,5)))#size of figure(x,y)
print(plt.plot(time,temperature,marker="d",mfc="r",mec="k",ms=15))
print(plt.title(f"Current Temperature & Time Forecast for {CITY_NAME}",fontdict=f1))
print(plt.xlabel("TIME",fontdict=f2))
print(plt.ylabel("TEMPERATURE(0°C)",fontdict=f3))
print(plt.grid())
print(plt.show())
