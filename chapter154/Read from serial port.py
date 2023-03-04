import serial
from serial import Serial
ser = serial.Serial('/dev/ttyUSB0', 9600)

#to read given number of bytes from the serial device
data = ser.read(size=5)
print(data)
#to read one line from serial device.
data1 = ser.readline()
print(data1)