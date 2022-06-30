import logging

from tests.features.initialize_consumer_producer import consumer_producer_instance


class ConsumerBroker:
    def __init__(self):
        self.broker = consumer_producer_instance.consumer

    def check_connection(self):
        connected = self.broker.bootstrap_connected()
        print(connected)

    def get_topics(self):
        topics = self.broker.topics()
        print(topics)
        if not topics:
            raise RuntimeError()
