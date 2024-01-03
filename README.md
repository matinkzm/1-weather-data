# 1-weather-data

This project is first project from 30 Data Engineering project ideas from this link: https://medium.com/@luisprooc/30-data-engineering-project-ideas-9ecf0a70cbea

In this project , I wanted to create a small ETL Data pipeline so I used wttr.in API to get temperature for some random cities , saved raw data into a txt file , remove some redundant data by searching for "°C" pattern and save it into a temp file for other tasks.

After that i removed all the remaining redundant data(for some cities I had to do it twice) and save the city name and its temperature into a dataframe.

I wrote those last few lines because I wanted my IDE to print the dataframe completely.


ETL = extract , transform , load

extract : get temperatures for cities
transform : remove redundant data
load : bring the data into a dataframe