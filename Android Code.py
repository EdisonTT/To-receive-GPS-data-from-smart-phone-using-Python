import androidhelper as android
import time
import socket
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("192.168.43.70",port)) #Ip address of the connected network
droid = android.Android()
while True:
    droid.startLocating(minDistance=1000,minUpdateDistance=1)
    droid.eventWaitFor('location', int(9000))
    location = droid.readLocation().result
    data = bytes(str(location),'ascii')
    s.send(data)
    print(location)
    time.sleep(3)    
droid.stopLocating()
