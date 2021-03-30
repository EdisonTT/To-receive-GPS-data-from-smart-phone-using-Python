# To-receive-GPS-data-from-smart-phone-using-Python

The program on the android device will collect all available information regarding the cell location. Location information is collected from the GPS as well as from the network.  Then, the collected data is sent to another device using wireless communication. <br />
The python program is run on the android device using Qpython. <br />
Qpython [download link](https://play.google.com/store/apps/details?id=org.qpython.qpy3&hl=en_IN&gl=US).<br />

The Python program for the Android device:
```python
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
The socket module is used to establish a connection between an android device and a Laptop (Wireless device).<br/>
To know more about socket module, see the documentaion [here](https://docs.python.org/3/library/socket.html#socket.socket.listen).<br/>
The andriodhelper moudle is used to access different status of the android device.<br/>
To know more about androidhelper module, see the details [here](https://github.com/isislovecruft/android-locale-hack).
```python
location = droid.readLocation().result
```
This method ```readlocation()```, will collect the location information from all available sources and returns a dictionary . A sample data is shown below.
```python
{'gps': {'altitude': -66.24295043945312, 'latitude': 10.59111675, 'longitude': 76.2170966, 'time': 1616769609000, 'accuracy': 3.2160000801086426, 'speed': 0, 'provider': 'gps', 'bearing': 0}, 'network': {'altitude': 0, 'latitude': 10.5894624, 'longitude': 76.214415, 'time': 1616769602806, 'accuracy': 1500, 'speed': 0, 'provider': 'network', 'bearing': 0}}
```
This dictionary  is converted to string and then converted to bytes. After that, it is sent to the Laptop. In this program, the location information is sent once in every three seconds. The rate can be varied by changing the argument inside ```time.sleep()```.<br/>

Python program for Laptop.
```python
import socket as soc
s = soc.socket()
host = '192.168.43.70'
port = 12345
s.setsockopt(soc.SOL_SOCKET, soc.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)
c,addr = s.accept()
while True:
    print(c.recv(2048).decode('ascii'))
```
Sample output is shown below. Note that the reccived data is a string.
```python
'{'gps': {'altitude': -66.24295043945312, 'latitude': 10.59111675, 'longitude': 76.2170966, 'time': 1616769609000, 'accuracy': 3.2160000801086426, 'speed': 0, 'provider': 'gps', 'bearing': 0}, 'network': {'altitude': 0, 'latitude': 10.5894624, 'longitude': 76.214415, 'time': 1616769602806, 'accuracy': 1500, 'speed': 0, 'provider': 'network', 'bearing': 0}}'
```
Before running the program, ensure that both the devices are connected to the same network.
