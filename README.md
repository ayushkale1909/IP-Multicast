# IP-Multicast
Multicast Group Communication
## 1. Receiver.py

This script sets up a multicast receiver that listens for incoming messages from a specified multicast group and port. Upon receiving a message, it prints out the content to the terminal.

#### Usage 

    python Receiver.py

## 2. Receiver-with-logging.py

Enhanced version of the basic multicast receiver. 

### Implements proper error handling for potential exceptions.
### Uses Python's logging module for improved log message formatting and potential logging to external sources.
### Appends timestamps to incoming messages.

#### Usage 

    python Receiver-with-logging.py

## 3. sender.py

### Prompts the user to input a message, which is then sent to the specified multicast group and port.

#### Usage 

    python sender.py

## 4. auto-message-sender.py

### Automatically sends 50 sequential messages to the specified multicast group and port. 

#### Usage 

    python auto-message-sender.py

