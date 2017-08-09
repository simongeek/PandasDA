# Pandas + Seaborn tutorial on Weather data for San Francisco Bay Area in California

Project analysys the weather on [San Francisco Bay Area region in California](https://en.wikipedia.org/wiki/San_Francisco_Bay_Area), exactly for cities like San Francisco, San Mateo, Santa Clara, Mountain View and San Jose.
Data cleaning, manipulation and data transformation was done with use of [Pandas](http://pandas.pydata.org/) - powerful Python data analysis toolkit. 
Addionaly there are many visualization, where some of them were prepared with matplotlib and [seaborn](https://seaborn.pydata.org/) library.
This project will introduce us to the basics of Pandas concept such as: 
* [data frames](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html)
* [manipulation and data transformation](https://www.analyticsvidhya.com/blog/2016/01/12-pandas-techniques-python-data-manipulation/)
* data cleaning 
* draw conclusions etc

Why Pandas and Seaborn?
+ You can easily pass Pandas Data Frame to Seaborn
+ Plot data from interesting columns or rows

Sample plots:

![temperature](https://user-images.githubusercontent.com/11740059/27057008-8975a544-4fca-11e7-8f7c-33091ed7f21e.jpg)
![temphum](https://user-images.githubusercontent.com/11740059/27057007-896ecd6e-4fca-11e7-91b6-88b25cc4baa9.jpg)
![histogram](https://user-images.githubusercontent.com/11740059/27057006-89682f5e-4fca-11e7-983c-3c792115946b.jpg)

Simple Youtube presentation what type of visualization is generated:



## Project desciption

For further analysis, parameters were choosen:
* temperature [F]
* humidity [%]
* pressure [inHg]
* wind speed [MPH]
* gust speed [MPH]
* cloud level [0-10]
* visibility [%]
* events such as rain, fog, thunderstorm

## What will you learn?


You will learn:

* How to read CSV files into Pandas Data Frame
* How to clean the data, remove missing values, remove unused columns, replace names etc.
* How to create plots, histograms and heat maps based on Pandas Data Frame

## Project structure

The project contains two file, first contains raw CSV data taken from [U.S. Government's open data website](https://www.data.gov/). 
The second file is Python script with all the pandas and seaborn code:
* weather.csv - data file, generated from U.S. Government's open data website
* main.py - main file with analysis and plots

## Resources

* [Official Pandas Documentation](http://pandas.pydata.org/pandas-docs/stable/)
 (You can also download it in [PDF version](http://pandas.pydata.org/pandas-docs/stable/pandas.pdf))
* [Femi Anthony "Mastering Pandas"](https://www.packtpub.com/big-data-and-business-intelligence/mastering-pandas)
* [Michael Heydt "Learning Pandas"](https://www.amazon.com/Learning-Pandas-Python-Discovery-Analysis/dp/1783985127)

## Grab the code or run project in online IDE
* You can [download code from GitHub](https://github.com/simongeek/PandasDA)
* You can [run the project in your browser](https://plon.io/explore/pandas-seaborn-tutorial-on-weather-data-for-sa/VpQywmDRHVPRfxa3G)

