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
sf = data.loc[data['ZIP'] == 94107] # San Francisco ZIP Code
sm = data.loc[data['ZIP'] == 94063] # San Mateo ZIP Code
sc = data.loc[data['ZIP'] == 94301] # Santa Clara ZIP Code
mv = data.loc[data['ZIP'] == 94041] # Mountain View ZIP Code
sj = data.loc[data['ZIP'] == 95113] # San Jose ZIP Code

# Plots of min, max and mean temperature in Fahrenheit scale

plt.figure()
df1 = pd.DataFrame(sc, columns=['meanTemp'])
plt.plot(df1.as_matrix(),'-')
plt.grid(True)
plt.xlabel('Day')
plt.ylabel('Temp F')
plt.title('Fahrenheit Temperature')
plt.legend(["Mean T"])
plt.show()

# Set Up histogram of mean temperature in Bay Area cities





