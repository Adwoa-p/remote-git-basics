import paho.mqtt.client as mqtt
from gpiozero import LED
from time import sleep

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Here you can subscribe to whatever topics you like
    # use '#' for a 'wildcard' - subscribe to any messages
    #client.subscribe("glblcd/lightbulb")
    # client.subscribe("codex/p")
    # client.subscribe("glblcd/pokua")
    # client.subscribe("glblcd/register")
    client.subscribe("glblcd/brown")
    

led=LED(17)
def on_message(client, userdata, msg):
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")
    if msg.payload.decode("utf-8") == "on":
        led.on()
    elif msg.payload.decode("utf-8") == "off":
        led.off()
    else:
        print("Invalid input")

# led=LED(17)
# def on_message(client, userdata, msg):
#     print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")
#     if (msg.payload.decode("utf-8"))== 150:
#         print("Pressure is normal")
#         led.on()
#     elif (msg.payload.decode("utf-8")) >150:
#         print("Pressure is too high")
#         led.off()
#     else:
#         print("Pressure is too low")
        

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)
# client.connect("127.0.0.1", 1883, 60)

client.loop_forever()