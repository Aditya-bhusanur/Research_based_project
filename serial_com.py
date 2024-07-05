import serial
import time
ser= serial.Serial('REPLACE THIS WITH THE ACTUAL POART TO WHICH ARDUINO IS CONNECTED TO PI', 9600)
while True:
    try:
        data=ser.readline().decode().strip()
        if data:
            sensor_val=float(data)
            print("Data revived.")
    except Exception as e:
        print("Error reciving the data {e}! ")
    time.sleep(0.1)
