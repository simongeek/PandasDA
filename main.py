import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import date, datetime, time
import time


#Import USA Weather data from CSV file
data = pd.read_csv('weather.csv')

#Make variables some friendlier names for users
"""data['PDT'] = data['date']
data['Max TemperatureF'] = data['maxTemp']
data['Min TemperatueF'] = data['minTemp']
data['Mean TemperatureF'] = data['meanTemp']
data['Max Dew PointF'] = data['maxDew']
data['MeanDew PointF'] = data['meanDew']
data['Min DewpointF'] = data['minDew']
data['Max Humidity'] = data['maxHum']
data['Mean Humidity'] = data['meanHum']
data['Max Sea Level PressureIn'] = data['maxPress']
data['Mean Sea Level PressureIn'] = data['minPress']
data['Min Sea Level PressureIn'] = data['meanPress']
data['Max VisibilityMiles'] = data['maxVis']
data['Mean VisibilityMiles'] = data['meanVis']
data['Min VisibilityMiles'] = data['minVis']
data['Max Wind SpeedMPH'] = data['maxWind']
data['Mean Wind SpeedMPH'] = data['meanWind']
data['Max Gust SpeedMPH'] = data['maxGust']
data['PrecipitationIn'] = data['preIn']
data['CloudCover'] = data['cloud']
data['WindDirDegrees'] = data['WindDir']
"""
#Convert Date Format



#Remove the bad samples
data = data[(data['Max TemperatureF'] < 110) & (data['Min TemperatureF'] > 25)]

#Plots of min, max and mean temperature in Fahrenheit scale

plt.figure()
df1 = pd.DataFrame(data, columns=['Max TemperatureF', 'Min TemperatureF', 'Mean TemperatureF'])
plt.plot(df1, '-')
plt.axis([0,1850, 0, 140])
plt.grid(True)
plt.xlabel('Day')
plt.ylabel('Temp F')
plt.title('Fahrenheit Temperature')
plt.legend(["Max T", "Min T","Mean T"])
plt.show()

#List unique values on example column using drop_duplicates(We can also use unique())
df2 = pd.DataFrame(data, columns=['ZIP'])
u = df2.drop_duplicates(['ZIP'])
print(u)

#Replace ZIP Code to City name


#