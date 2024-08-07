import blynklib
from serial import SerialReader

#Setup auth token and virtual pin number fro Blynk app.
AuthToken="PLACE YOUR AUTH TOKEN HERE"
sensor_pin=Vx #REPLACE 'X' PIN NUMBER WITH YOUR VIRTUAL PIN NUMBER.

#Function for sending data to blynk app.
def send_data_to_blynk(value):
    if value is not None:
        blynk.virtual_write(sensor_pin, value)
blynk=blynklib.Blynk(AuthToken) #AUTH TOKEN

@blynk.handle_event('CONNECTED')
def handle_connected():
    print("Blynk connected!")
SerialReader=SerialReader()

@blynk.run(1000)
def loop():
    sensor_value=SerialReader.read_sensor_data()
    send_data_to_blynk(sensor_value)
blynk.run()