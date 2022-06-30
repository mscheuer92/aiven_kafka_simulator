import json
import logging
from kafka.structs import TopicPartition
from config import constant
from tests.features.initialize_consumer_producer import consumer_producer_instance
from tests.json_payload import PAYEE_DATA


class Consumer:
    def __init__(self):
        self.consumer = consumer_producer_instance.consumer

    def consumer_subscribe_and_verify_data(self):
        self.consumer.assign([TopicPartition(constant.TOPIC, 1)])
        for message in self.consumer:
            print(PAYEE_DATA)
            print(message.partition, message.offset, message.value)

            # consumer_message is type String. Convert to dictionary for comparison with PAYEE_DATA.
            consumer_string_to_dictionary = json.loads(message.value)
            assert PAYEE_DATA == consumer_string_to_dictionary

            # # Compare by converting to set
            set_1 = set(consumer_string_to_dictionary)
            set_2 = set(PAYEE_DATA)
            assert set_1 == set_2
            self.consumer.close()

            logging.info(message.offset, message.partition, message.value)
            self.consumer.close()
