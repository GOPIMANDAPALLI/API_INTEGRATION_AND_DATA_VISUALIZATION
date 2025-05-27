import matplotlib.pyplot as plt

#enter city name from the user

CITY_NAME=input("enter the city name :")

#extract temperature and time

temperature=[25.0,21.2,10.4,32.3,15.5,30.0]
time=[6.00,7.00,8.00,9.00,10.00,11.00]

#addig color,size and family to the text

f1={'family':'arial','color':'c','size':20}
f2={'family':'arial','color':'b','size':20}
f3={'family':'arial','color':'b','size':20}


print(plt.figure(figsize=(10,5)))#size of figure(x,y)
print(plt.plot(time,temperature,marker="o",mfc="r",mec="k",ms=15))
print(plt.title(f"24-Hour Temperature Forecast for {CITY_NAME}",fontdict=f1))
print(plt.xlabel("TIME",fontdict=f2))
print(plt.ylabel("TEMPERATURE",fontdict=f3))
print(plt.grid())
print(plt.show())
