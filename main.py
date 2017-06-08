import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import date, datetime, time
import time
import seaborn as sns

# Import San Francisco Bay Area Weather data from CSV file
data = pd.read_csv('weather.csv')

# Make variables some friendlier names for users
old_names = ['Max TemperatureF', 'Min TemperatureF', 'Mean TemperatureF', 'Max Dew PointF', 'MeanDew PointF',
             'Min DewpointF', 'Max Humidity',
             ' Mean Humidity', ' Min Humidity', ' Max Sea Level PressureIn', ' Mean Sea Level PressureIn',
             ' Min Sea Level PressureIn', ' Max VisibilityMiles', ' Mean VisibilityMiles',
             ' Min VisibilityMiles', ' Max Wind SpeedMPH', ' Mean Wind SpeedMPH', ' Max Gust SpeedMPH', 'PrecipitationIn',
             ' CloudCover', ' WindDirDegrees', ' Events']
new_names = ['maxTemp', 'minTemp', 'meanTemp', 'maxDew', 'meanDew', 'minDew', 'maxHum', 'meanHum', 'minHum', 'maxPress',
             'minPress', 'meanPress', 'maxVis', 'meanVis',
             'minVis', 'maxWind', 'meanWind', 'maxGust', 'preIn', 'cloud', 'WindDir', 'events']
data.rename(columns=dict(zip(old_names, new_names)), inplace=True)


# Delete unused column in CSV File

del data['preIn']

# Remove the bad samples in temperature
data = data[(data['maxTemp'] <= 110) & (data['minTemp'] >= 25)]

# List unique values on example column using drop_duplicates(We can also use unique())
df2 = pd.DataFrame(data, columns=['ZIP'])
u = df2.drop_duplicates(['ZIP'])



# Get data for cities
# 94107 -> San Francisco
# 94063 -> San Mateo
# 94301 -> Santa Clara
# 94041 -> Mountain View
# 95113 -> San Jose
zipcodes = [94107, 94063, 94301, 94041, 95113]

# Day of months: start September, end August
x = [30, 61, 91, 122, 153, 182, 213, 243, 274, 304, 335, 366]
labels = ['September','October','November','December','January','February','March','April','May','June','July','August']

# Plots of Mean temperature in Fahrenheit scale

plt.figure()
for zcode in zipcodes:
  local = data.loc[data['ZIP'] == zcode]
  df1 = pd.DataFrame(local, columns=['meanTemp'])
  plt.plot(df1.as_matrix(), '-', label=str(zcode))

plt.xticks(x,labels,rotation='vertical',fontsize=12)
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('Temperature in Fahrenheit scale', fontsize=15)
plt.title('Fahrenheit Mean Temperature on Bay Area Cities',fontsize=20)
plt.legend(["San Francisco", "San Mateo","Santa Clara", "Mountain View","San Jose"])
plt.show()

# Plot compare Mean Wind and Max Gust

plt.figure()
for zcode in zipcodes:
    mw = data.loc[data['ZIP'] == zcode]
    df3 = pd.DataFrame(mw, columns=['meanWin', 'maxGust'])
    plt.plot(df3.as_matrix(),'-', label=str(zcode))

plt.xticks(x,labels,rotation='vertical', fontsize=12)
plt.grid(True)
plt.xlabel('Month')
plt.ylabel('MPH', fontsize=15)
plt.title('Mean Wind and Max Gust', fontsize=20)
plt.legend(["Mean Wind","Max Gust"])
plt.show()

# Plot mean temperature with mean humidity for San Francisco

sf = data.loc[data['ZIP'] == 94107]
plt.figure()
df4 = pd.DataFrame(sf, columns=['meanTemp','meanHum'])
plt.plot(df4.as_matrix(), '-')
plt.grid(True)
plt.autoscale()
plt.xlabel('Month')
plt.ylabel('x', fontsize=15)
plt.title('',fontsize=20)
plt.xticks(x,labels,rotation='vertical', fontsize=12)
plt.legend(["Mean Temp", "Mean Humidity"])
plt.show()

# replace '' string with blank values to zero in CSV file

data.fillna(0, inplace=True)


# Correlation between two columns
"""
sns.lmplot(x='meanTemp', y='meanHum', data=data)
plt.show()
"""

# Histogram of Mean Temperature in All cities in Bay Area

plot_hist = plt.hist(data['meanTemp'], bins=10)
plt.xlabel('Temperature [F]')
plt.ylabel('Amount')
plt.show()


# Plot Area compare Cloud Level and Event such as rain, rain-thunderstorm, fog or fog-rain example for San Francisco

data['events'].replace(['Rain','Rain-Thunderstorm','Fog','Fog-Rain'],[1,1,0,1],inplace=True)
sf = data.loc[data['ZIP'] == 94107]
df7 = pd.DataFrame(sf, columns=['cloud','events'])
df7.plot.area(stacked=False)
plt.xlabel('Month')
plt.ylabel('Cloud Level', fontsize=18)
plt.title('Cloud Level with Events: Rain, Storm, Fog etc.',fontsize=20)
plt.xticks(x,labels,rotation='vertical', fontsize=12)
plt.legend(["Cloud","Rain: 1-yes, 0-no"])
plt.show()


# Plot of min, max and mean pressure for San Francisco


sf = data.loc[data['ZIP'] == 94107]
plt.figure()
df8 = pd.DataFrame(sf, columns=['minPress','meanPress','maxPress'])
plt.plot(df8.as_matrix(), '-')
plt.grid(True)
plt.autoscale()
plt.xlabel('Month')
plt.ylabel('inHg', fontsize=18)
plt.title('Min, Mean and Max Pressure for San Francisco',fontsize=20)
plt.xticks(x,labels,rotation='vertical', fontsize=12)
plt.legend(["Minimum Pressure", "Mean Pressure","Maximum Pressure"])
plt.show()


# Plot of Rain and humidity


plt.figure()
df9 = pd.DataFrame(sf, columns=['events','meanHum'])
plt.plot(df9, '-')
plt.xlabel('Month')
plt.ylabel('')
plt.title('Plot compare Events such as Rain, Fog etc. with mean Humidity', fontsize=20)
plt.xticks(x,labels,rotation='vertical', fontsize=12)
plt.legend(["Rain?", "Mean Humidity"])
plt.show()


# Area Plot compare Cloud Lever and Visibility

"""

Poniższą wizualizację chcę zaprezentować w inny sposób(którą chcę z Panem skonsultować), poniższa to tylko 
wersja robocza.


"""
df10 = pd.DataFrame(sf, columns=['cloud','minVis'])
df10.plot.area(stacked=False)
plt.xlabel('Month')
plt.ylabel('')
plt.title('Plot compare Cloud Level and Mean Visibility', fontsize=20)
plt.xticks(x,labels,rotation='vertical', fontsize=12)
plt.legend(["Cloud Lever","Mean Visibility"])
plt.show()



"""

Chcę jeszcze zademonstrować wizualizację za pomocą Heat Map* oraz innych rodzajów wykresów takich jak scatter, aby
wykorzystać bardziej Pandas i jej możliwości.


*Czy jest też sens robienia heatmap dla tych danych? Musiałbym wycinać dane np. dla jednego miesiąca, czy nawet
tygodnia, aby było cokolwiek widać.

"""


# Print all data from CSV file
print(data)