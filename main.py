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
             'Mean Humidity', 'Min Humidity', 'Max Sea Level PressureIn', 'Mean Sea Level PressureIn',
             'Min Sea Level PressureIn', 'Max VisibilityMiles', 'Mean VisibilityMiles',
             'Min VisibilityMiles', 'Max Wind SpeedMPH', 'Mean Wind SpeedMPH', 'Max Gust SpeedMPH', 'PrecipitationIn',
             'CloudCover', 'WindDirDegrees']
new_names = ['maxTemp', 'minTemp', 'meanTemp', 'maxDew', 'meanDew', 'minDew', 'maxHum', 'meanHum', 'minHum', 'maxPress',
             'minPress', 'meanPress', 'maxVis', 'meanVis',
             'minVis', 'maxWind', 'meanWind', 'maxGust', 'preIn', 'cloud', 'WindDir']
data.rename(columns=dict(zip(old_names, new_names)), inplace=True)



# Remove the bad samples in temperature
data = data[(data['maxTemp'] <= 110) & (data['minTemp'] >= 25)]

# List unique values on example column using drop_duplicates(We can also use unique())
df2 = pd.DataFrame(data, columns=['ZIP'])
u = df2.drop_duplicates(['ZIP'])
print(u)


# Get data for cities
# 94107 -> San Francisco
# 94063 -> San Mateo
# 94301 -> Santa Clara
# 94041 -> Mountain View
# 95113 -> San Jose
zipcodes = [94107, 94063, 94301, 94041, 95113]

# Plots of Mean temperature in Fahrenheit scale

plt.figure()
for zcode in zipcodes:
  local = data.loc[data['ZIP'] == zcode]
  df1 = pd.DataFrame(local, columns=['meanTemp'])
  plt.plot(df1.as_matrix(), '-', label=str(zcode))
plt.grid(True)
plt.xlabel('Day')
plt.ylabel('Temperature in Fahrenheit scale')
plt.title('Fahrenheit Mean Temperature on Bay Area Cities')
plt.legend(["San Francisco", "San Mateo","Santa Clara", "Mountain View","San Jose"])
plt.show()

# Plot compare Mean Wind and Max Gust


