# To-receive-GPS-data-from-smart-phone-using-Python

The program on the android device will collect all available information regarding the cell location. Location information is collected from the GPS as well as from the network.  Then, the collected data is sent to another device using wireless communication. <br />
The python program is run on the android device using Qpython. <br />
Qpython [download link](https://play.google.com/store/apps/details?id=org.qpython.qpy3&hl=en_IN&gl=US).<br />

The Python program for the Android device:
```
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
```
