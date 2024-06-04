# USB port

after opening the Trifo max model two USB ports were found. one USB A, and one micro usb port.

# USB A
this port does not seem not to be connected. If a keyboard is connected and the capslock key is pressed, the capslock indicator does not turn on.


# Micro USB (picture available [here](https://github.com/VictorDrijkoningen/trifo-robotics-rev-eng/blob/04a331fae4f84ecbf3329fd335d6889a67002bb7/Trifo-Max%20V1.1%20Pictures/Main%20Chips.jpg) )
when the Max model is turned on and the micro usb port is connected to a computer, the computer does not see the max model in any way. This seems to suggest there is another protocol on this port.


# Other connections:
There are also some places where headers could be soldered:

```
back (dustbbin)

 ...  (UART TX 115200 baud | 3.3v when robot is on uart rx?? | ground)

....  ( just 3.3v during boot | just 3.3v during boot | kinda ground? | ground) spi?? 

 ...  ( sdio? | sdio? | ground) this is connected to the wifi chip, which has a sdio connection

front (bumper)
```

the uart prints this:

```
/***************************************/
/***********Trifo robotics.*************/
/***************************************/
Info: enter bootloader.....
Info: bootloader version:v2.1.1
Info: wait key input.
Info: load user application...
```
and keystrokes don't seem to do anything.
