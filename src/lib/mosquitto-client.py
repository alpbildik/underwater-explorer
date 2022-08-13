import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

BROKER_IP = 'localhost'


class TopicCallbackPair:
    def __init__(self, topicname, callback_fun):
        self.topicname = topicname
        self.callback_fun = callback_fun


class MessageSubscriber():
    def __init__(self, name):
        #Initiate mqtt client
        self.client =  mqtt.Client(name)


    """
        topic: 'sensors/#'
        listeners: [{
                topicname: 'sensors/humidity'
                callback_fun: humidity_sensor_fun
            }]

    """
    def subscribe(self, topic, listeners: [TopicCallbackPair], is_async=False):
        for listener in listeners:
            self.client.message_callback_add(listener.topicname, listener.callback_fun)

        self.client.connect(BROKER_IP)
        self.client.subscribe(topic)

        if is_async :
            self.client.loop_start()
        else:
            self.client.loop_forever()

    @classmethod
    def publish_single(cls, topic, message):
        publish.single(topic=topic, payload=message, hostname=BROKER_IP)




if __name__ == '__main__':
    def listener_1(client, userdata, msg):
        print('listener_1 receieved: ', msg.payload)

    def listener_2(client, userdata, msg):
        print('listener_2 receieved: ', msg.payload)

    subscriber = MessageSubscriber('test_subscriber')
    subscriber.subscribe('test/#', [TopicCallbackPair('test/topic1', listener_1), TopicCallbackPair('test/topic2', listener_2)], is_async=True)
    MessageSubscriber.publish_single('test/topic1', 'message_1')
    MessageSubscriber.publish_single('test/topic2', 'message_2')
