import time
import paho.mqtt.client as mqtt_client
import random
import serial

def get_connection(port):
    ser = serial.Serial(port, timeout=1)
    return ser

broker = "broker.emqx.io"

client = mqtt_client.Client(f'lab_{random.randint(10000, 99999)}')

try:
    client.connect(broker)
except Exception:
    print('Failed to connect. Check network.')
    exit()

# add port
ser = get_connection('')

while True:
    if ser.in_waiting > 0:
        data = ser.read(1)
        print(ord(data))
        client.publish('iot/lab/sensor', str(ord(data)))
    time.sleep(0.1)