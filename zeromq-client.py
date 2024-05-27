import json
import zmq


# .env file looks like this: {"ROBOTIP": "someip", "PORT": "7777"}

with open('.env', encoding='utf-8') as f:
    env = json.loads(f.read())



# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://"+env['ROBOTIP']+":"+env['PORT'])


sock.send(b"a")

message = sock.recv()
print(message)
