# ZeroMQ ZMTP server

the python code in the repo works with connecting to the Trifo Max robot. When a binary b'a' is sent the result is:

```
a\x00
```

so it repeats whatever is sent + \x00, except if more than one byte is sent. In this case the robot only repeats the first byte (i think).

the byte \r seems to have some other pattern applied. some more bytes are returned in this case