from tests.features.consumer.consumer_broker import ConsumerBroker
from tests.features.consumer.kafka_consumer_class import Consumer
from tests.features.producer.kafka_producer_class import Producer

p = Producer()
c = Consumer()

p.producer_send_data()
p.verify_offset_partition_presence()
p.flush_producer()
p.producer_graceful_exit()

c.consumer_subscribe_and_verify_data()

b = ConsumerBroker()
b.check_connection()
b.get_topics()
