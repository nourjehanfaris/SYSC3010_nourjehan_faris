from urllib.request import * 
from urllib.parse import * 
import json
import sqlite3

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa


# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
  # results is a JSON string
webData.close()

print (results)
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results

current = data["main"]
degreeSym = chr(176)

temp = current["temp"]
humid = current["humidity"]
press = current["pressure"]

print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
print ("Humidity: %d%%" % current["humidity"])
print ("Pressure: %d" % current["pressure"] )

current = data["wind"]

wind = current["speed"]

print ("Wind : %d" % current["speed"])

#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");

dbconnect.row_factory = sqlite3.Row;

cursor = dbconnect.cursor()
cursor.execute("BEGIN;")
cursor.execute("CREATE TABLE IF NOT EXISTS cityWeather(City TEXT, Temperature NUMERIC, Humidity NUMERIC, Pressure NUMERIC, WindSpeed NUMERIC)")
cursor.execute("COMMIT;")
cursor.execute("INSERT INTO cityWeather(City, Temperature, Humidity, Pressure,WindSpeed) VALUES(?,?,?,?,?)", (city,temp,humid,press,wind))

cursor.execute("SELECT * FROM cityWeather")

for row in cursor:
    print(row['City'],row['Temperature'],row['Humidity'],row['Pressure'],row['WindSpeed']);

dbconnect.commit() # commit all changes to database
dbconnect.close();

