# Created by Michelle Scheuer at 6/16/22
Feature: Produce and Consume Payee Data

  Scenario: Happy Path - Produce and Consume Payee Data
    When I send a message to the Aiven-Kafka producer with PAYEE_DATA
    Then I should receive a partition and an offset
    When I verify the consumer data matches the producer data
