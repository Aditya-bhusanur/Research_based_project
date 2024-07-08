import serial

class SerialReader:
    #Function for defining poart and buad rate.
    def __init__(self, port='/dev/ttyUSB0', baud_rate=9600): #REPLACE THE POART WITH THE ACTUAL POART TO WHICH ARDUINO IS CONNECTED TO PI
        self.ser=serial.Serial(port, baud_rate)

    #function for reciving data and decoding.
    def read_sensor_data(self):
        try:
            data=self.ser.readline().decode('ascii').strip()
            if data:
                sensor_value=float(data)
                return sensor_value
            else:
                return None
        #Exception handling.
        except Exception as e:
            print(f"Error reading serial data: {e}")
            return None
       

