# ZeroMQ ZMTP server

the python code in the repo works with connecting to the Trifo Max robot. When a binary b'a' is sent the result is:

```
a\x00
```

so it repeats whatever is sent + \x00, except if more than one byte is sent. In this case the robot only repeats the first byte (i think).

the byte \r seems to have some other pattern applied. some more bytes are returned in this case:

```
b'\r\x00\x00\xff'
```

after, i ran a selfmade fuzzer script, which tried every combination of two bytes, i suspect there's some sort of password needed, afterwhich more interesting thing would happen. or i'm missing something else