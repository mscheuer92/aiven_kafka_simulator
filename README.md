# Kafka Based Testing Example

### About:
This project was created to understand how to test Kafka based systems using Python and Cucumber 
Behavior Driven Development (BDD) framework. One of the goals for my team in 2022 was to be able to successfully test the Kafka
side of several business services.

Projects must be running on Aiven-Kafka for this program to function correctly.

### Setup
* You will need to download Kafka if it is not already on your machine.
  ```console
  pip install kafka
  ```
  You may also need to install:
  ``` console
  pip install kafka-python
  ```
#### Project Settings
* `config/constant.py` contains all of the variables needed to run this program. All of the values can be found in Aiven. You will need
to set the variables accordingly before running.

* Aiven certificates needed:`ca.pem`, `ca.cert`, and `secret.key`. These go in the `aiven_certificates` directory.
  * Click the "Privatelink" radio button in the Apache Kafka tab.
  * Copy the CA Certificate into the `ca.pem` file.
  * Click the appropriate Kafka service
  * Click on the "Users" tab
  * Find the user and copy the access key into the `secret.key` file. Copy the access cert into the `ca.cert` file.
* You can find the `TOPIC` value in Aiven. The topic will need to be relevant to what it is you're trying to connect to.
* You will also need to find the consumer group ID if you choose to use it, and set

### Running
* First, you will need to create mock json data. In the original program, I've left the schema for the "PAYEE_DATA". Change the 
variable and data to whatever you'd like to send. If you have access to the WEX Inc VPN, you should be able to run this program as is.
  * In that instance, connect to the VPN and ensure you are connected to "Portland HQ Gateway".

#### Outside a Docker Container
This program can run 2 different ways. By executing `python3 main.py`, the program does not use BDD framework. This
file was included because it is valuable for testing purposes. It will test the producer, consumer, and the connection to the consumer's broker.


#### Inside a Docker Container
Running this program inside a Docker Container is for if you want to run the feature files. This specific feature file was 
written for a service called "Payee Service". Features and steps will need to be altered for any other project.


### Troubleshooting
If you are receiving a "NoBrokersAvailable" message:
  * Make sure you are connected to the VPN (For Wex projects)
  * Make sure you are connected to Portland HQ Gateway and not Portland HQ2 Gateway.
