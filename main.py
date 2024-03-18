import paho.mqtt.client as mqtt

def ao_conectar(client, userdata, flags, rc):
print("Nos conectamos com o seguinte código de resultados{}".format(srt(rc)))

def ao_receber(client(client, userdata, msg):
print("{} --- {}".format(msg.topic, srt(msg.payload)))

cliente = mqtt.CLient()

client.on_connect = ao_conectar
client.on_connect = ao_receber

client.on_connect ("blocker.hivemq.com", 1883, 60)
client.subscriber("aula3b")
cliente.loop_forever()
