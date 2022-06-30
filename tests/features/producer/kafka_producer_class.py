from datetime import date
from kafka.future import log

from tests import json_payload
from tests.features.initialize_consumer_producer import consumer_producer_instance
from tests.json_payload import PAYEE_DATA


class Producer:
    partition_data = []
    offset_data = []

    def __init__(self):
        self.producer = consumer_producer_instance.producer

    def on_send_success(self, record_metadata):
        # Get producer metadata information. The partition and offset should match the output of the consumer
        print("producer topic: ", record_metadata.topic)
        print("producer partition: ", record_metadata.partition)
        print("producer offset: ", record_metadata.offset)

        part = record_metadata.partition
        offset = record_metadata.offset
        self.partition_data.append(part)
        self.offset_data.append(offset)

    def verify_offset_partition_presence(self):
        assert self.partition_data is not None
        assert self.offset_data is not None

    def on_send_error(self, excp):
        log.error('Producer failure', exc_info=excp)

    def producer_send_data(self):
        # # add_callback() calls on_send_success so that if the
        # producer is successful, the metadata will be displayed
        self.producer.send('payments.principals', value=PAYEE_DATA, partition=1).add_callback(self.on_send_success).add_errback(
            self.on_send_error)

    def flush_producer(self):
        # Print message to show that we're at least attempting to send a message
        print(
            f'Producing message @ {date.today()} | Message = {str("Sending message for partition: " + json_payload.first_name + " " + json_payload.last_name)}')

        # Flush producer twice to make sure message actually sends
        self.producer.flush()

    def producer_graceful_exit(self):
        self.producer.close()
