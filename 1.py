import fastapi
from kafka import KafkaProducer, KafkaConsumer


app = fastapi.FastAPI()

# Create a Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Create a topic for each type of message
topic_high = 'high-priority'
topic_low = 'low-priority'

# Define a route for the `/publish` endpoint
@app.get('/publish')
def publish(message: str, topic: str):
    # Produce the message to Kafka
    if topic == 'high-priority':
        priority = 1
    else:
        priority = 0
    producer.send(topic, message.encode('utf-8'), priority=priority)
    return {'message': 'Message published successfully!'}

# Define a route for the `/change_topic` endpoint
@app.get('/change_topic')
def change_topic(message_id: int, new_topic: str):
    # Get the message from Kafka
    message = producer.get(message_id)

    # Change the topic of the message
    message.set_topic(new_topic)

    # Produce the message to Kafka
    producer.send(new_topic, message.encode('utf-8'))
    return {'message': 'Message topic changed successfully!'}

if __name__ == '__main__':
    app.run(debug=True)