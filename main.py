import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt



#Import USA Weather data from CSV file

data = pd.read_csv('weather.csv')

#Delete unused column

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
plt.legend(["Max T", "Min T","Mean T","Humidity"])
plt.show()

#List unique values on example column using drop_duplicates(We can also use unique())
df2 = pd.DataFrame(data, columns=['ZIP'])
u = df2.drop_duplicates(['ZIP'])
print(u)

#Replace ZIP Code to City name


#