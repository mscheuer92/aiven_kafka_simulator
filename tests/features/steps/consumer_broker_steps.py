from behave import *

from tests.features.consumer.consumer_broker import ConsumerBroker

consumer_broker = ConsumerBroker()


@when("The consumer is connected to a broker")
def consumer_broker_connection(context):
    consumer_broker.check_connection()


@then("The broker should return all topics")
def return_topics(context):
    consumer_broker.get_topics()
