raspberry pi mqtt



import paho.mqtt.client as mqtt #import the client1
import time
############


def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


########################################
broker_address="192.168.xx.xxx"  # your broker adress
print("creating new instance")

client = mqtt.Client("P1") #create new instance

client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker


client.subscribe("pc")
client.publish("raspi","hello from raspi")

client.loop_start() #start the loop
