from behave import *

from tests.features.consumer.kafka_consumer_class import Consumer
from tests.features.producer.kafka_producer_class import Producer

producer = Producer()
consumer = Consumer()


@when("I send a message to the Aiven-Kafka producer with PAYEE_DATA")
def step_impl(context):
    producer.producer_send_data()


@then("I flush the producer")
def step_impl(context):
    producer.flush_producer()


@then("I gracefully exit the producer")
def step_impl(context):
    producer.producer_graceful_exit()


@then("I should receive a partition and an offset")
def step_impl(context):
    producer.verify_offset_partition_presence()


@when("I verify the consumer data matches the producer data")
def step_impl(context):
    consumer.consumer_subscribe_and_verify_data()
