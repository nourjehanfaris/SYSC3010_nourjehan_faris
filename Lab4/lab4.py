import http.client
import urllib.parse

key = "54CDA6FJF4RCJ92C"
cmail= "nourjehanfaris@cmail.carleton.ca"
group= "L2-M-7"
memberID= "b"

params = urllib.parse.urlencode({'field1': cmail, 'field2': group, 'field3':memberID, 'key':key})

headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept":"text/plain"}

conn = http.client.HTTPConnection("api.thingspeak.com:80")

try:
    conn.request("POST","/update",params,headers)
    response = conn.getresponse()
    print(cmail)
    print(group)
    print(memberID)
    print(response.status,response.reason)
    data = response.read()
    conn.close()
    
except:
    print("connection failed")

