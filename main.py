import os
import pandas as pd

# generate 100 comma seperated city name using this link : https://commentpicker.com/random-capital-generator.php
city_string = "San Juan, Reykjavik, Kiev, Athens, Dakar, Monrovia, Moscow, Copenhagen, Palikir, Kuwait City, Yamoussoukro, Havana, Noumea, Dhaka, Rabat, Montevideo, Doha, Avarua, Fort-de-France, Athens, Port Vila, Vientiane, Amsterdam, Islamabad, Port Louis, Islamabad, Macao, Rome, Riyadh, Suva, Havana, Longyearbyen, Accra, Flying Fish Cove, Basse-Terre, Georgetown, Apia, Nassau, Andorra la Vella, Yamoussoukro, Khartoum, Basseterre, New Delhi, Tbilisi, Male, Rabat, Jamestown, Accra, Oranjestad, Tegucigalpa, Baghdad, Funafuti, Pyongyang, Muscat, Niamey, Pretoria, Minsk, Ankara, Oranjestad, Sofia, Monaco, Gibraltar, Singapur, Washington, Ashgabat, Addis Ababa, Prague, Taipei, Abu Dhabi, Podgorica, Helsinki, Skopje, Vienna, Banjul, Paramaribo, Pristina, East Jerusalem, St. George's, Banjul, Warsaw, Willemstad, Bissau, Suva, The Valley, Guatemala City, Managua, Plymouth, Yamoussoukro, Willemstad, Kuala Lumpur, East Jerusalem, Belmopan, Podgorica, Islamabad, Astana, Paris, Jakarta, Maputo, Santo Domingo, Kingstown"

# remove redundant spaces
city_string = city_string.replace(" ", "")

# separate each city with comma
city_list = city_string.split(",")

data_dict = {}

for city in city_list:
    # download weather data from wttr for each city
    command = "curl -o weatherData.txt wttr.in/" + city
    os.system(command)

    # remove redundant data and search for lines with °C sign
    os.system("grep '°C' weatherData.txt > temp.txt")

    # read each line and search for temperature among raw data
    with open("temp.txt") as file:
        line = str(file.readline().splitlines())
        place = -1
        for i in range(0, 3):
            place = line.find('m', place + 1)
        place += 1
        temperature = ""
        while True:
            if line[place] != "\\":
                temperature += line[place]
                place += 1
            else:
                break

        # if the temperature was empty search again for temperature among raw data
        if temperature == " ":
            place = line.find('m', place + 1)
            place += 1
            temperature = ""
            while True:
                if line[place] != "\\":
                    temperature += line[place]
                    place += 1
                else:
                    break

        # create a dictionary for city and its temperature
        data_dict[city] = temperature

# convert dictionary into dataframe
dataframe = pd.DataFrame(list(data_dict.items()), columns=['city_name', 'temperature'])

# used this command to print the dataframe completely
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
    print(dataframe)
