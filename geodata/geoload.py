import urllib.request, urllib.parse
import sqlite3
import json

api_key = False
if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Locations")

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open("where.data","w")
address = input('Enter location: ')
if len(address) < 1:
    print("Please enter valid location.")

fh.write(address)
fh.close()

fh = open("where.data", "r")
for line in fh:

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass

    parms = dict()
    parms["address"] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    #print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    conn.commit()


print("Run geodump.py to read the data from the database so you can vizualize it on a map.")