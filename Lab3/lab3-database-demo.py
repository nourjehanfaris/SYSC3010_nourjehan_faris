import sqlite3
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();
#execute simple select statement
cursor.execute('SELECT * FROM temps');
#print data from temps
for row in cursor:
    print(row['tdate'],row['ttime'],row['zone'],row['temperature'] );

#now we create a second cursor to work with db for the sensors table
cursor2 = dbconnect.cursor();
#execute simple select statement
cursor2.execute('SELECT * FROM sensors');
#print data from sensors
for row in cursor2:
    print(row['sensorID'],row['type'],row['zone'] );

#displays all sensors in the kitchen only:
print("Sensors in the kitchen:");
cursor2.execute('SELECT * FROM sensors WHERE zone="kitchen"');
for row in cursor2:
	print(row['sensorID'],row['type'],row['zone'] );


#displays all door sensors only:
print("Door sensors:");
cursor2.execute('SELECT * FROM sensors WHERE type="door"');
for row in cursor2:
        print(row['sensorID'],row['type'],row['zone'] );

#close the connection
dbconnect.close();

