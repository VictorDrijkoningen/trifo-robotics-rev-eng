import json
import zmq
import time
import datetime


# .env file looks like this: {"ROBOTIP": "someip", "PORT": "7777"}

with open('.env', encoding='utf-8') as f:
    env = json.loads(f.read())



# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://"+env['ROBOTIP']+":"+env['PORT'])

options = [x.to_bytes(2) for x in range(2**16)]
interesting_finds = list()
length = len(options)
count = 0

for num,t in enumerate(options):
    # print(str(t) + " gives:")
    if count > 100:
        print(num / length)
        count = 0
    count += 1
    sock.send(b"%s" % t)
    time.sleep(0.03)
    message = sock.recv()
    if (not message == (t[:1] + b'\x00')):
        print(t)
        print("gives:")
        print(message)
        print()
        interesting_finds.append(t)

with open("out.txt", encoding='utf-8', mode='a') as f:
    f.write(str(datetime.datetime.today()) + " | ")
    f.write(json.dumps(str(interesting_finds)))
    f.write("\n")