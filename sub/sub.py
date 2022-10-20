from http import client
import time
import paho.mqtt.client as mqtt_client
import random
import serial


def get_connection(port):
    ser = serial.Serial(port, timeout=1)
    return ser

def on_message(client, userdata, message):
    data = str(message.payload.decode("utf-8"))
    topic = str(message.topic.encode("utf-8"))
    print(f"Received message on {topic}: {data}")
    ser.write(bytearray([int(data)]))

broker = "broker.emqx.io"

client = mqtt_client.Client(f'lab_{random.randint(10000,99999)}')
client.on_message = on_message

try:
    client.connect(broker)
except Exception:
    print('Failed to connect. Check network.')
    exit()

client.loop_start()

print('Subscribing')
client.subscribe('iot/lab/sensor')

ser = get_connection('COM9')

time.sleep(600)
client.disconnect()
client.loop_stop()
print('Stop communcation')