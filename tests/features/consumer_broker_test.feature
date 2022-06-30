# Created by Michelle Scheuer at 6/16/22
Feature: Test Consumer Broker Connection

  Scenario: Happy Path - Consumer Broker Connection
      When The consumer is connected to a broker
      Then The broker should return all topics