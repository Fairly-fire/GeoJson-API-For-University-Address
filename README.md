# GeoJson-API-For-University-Address
The project has been designed in a way that it plots university /college on a world map. It uses python programming language as the base to ask the user for a location, retrieve data, load the university name with location data into a database, then visualize that data on Google Maps.This project basically uses a GeoLocation lookup API modeled after the Google API to look up some universities and parse the returned data and return address of Universities over the world using Python .The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the formatted address, latitude and longitude from the JSON into a database file. The database software used in the project is SQLite. It stores data in Location table. The second python script is used to read the database and produce a JavaScript file. Finally, we have to open a HTML file to visualize the location markers in Google Maps.
