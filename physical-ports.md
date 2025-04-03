# USB port

after opening the Trifo max model two USB ports were found. one USB A, and one micro usb port.

# USB A
this port does not seem not to be connected. If a keyboard is connected and the capslock key is pressed, the capslock indicator does not turn on.


# Micro USB (picture available [here](https://github.com/VictorDrijkoningen/trifo-robotics-rev-eng/blob/04a331fae4f84ecbf3329fd335d6889a67002bb7/Trifo-Max%20V1.1%20Pictures/Main%20Chips.jpg) )
when the Max model is turned on and the micro usb port is connected to a computer, the computer does not see the max model in any way. When the SoC is in maskrom mode, it does work.


# Other connections:
There are also some places where headers could be soldered:

```
back (dustbbin)

 ...  (STM32 UART TX 115200 baud? | 3.3v when robot is on uart rx?? | ground)

....  ( just 3.3v during boot | just 3.3v during boot | kinda ground? | ground) ??

 ...  ( SoC UART TX 1500000 | SoC UART RX 1500000 | ground)

front (bumper)
```

the stm32 uart prints this:

```
/***************************************/
/***********Trifo robotics.*************/
/***************************************/
Info: enter bootloader.....
Info: bootloader version:v2.1.1
Info: wait key input.
Info: load user application...
```

the key that is referenced, is the home button on board. if pressed during boot:

```
/***************************************/
/***********Trifo robotics.*************/
/***************************************/
Info: enter bootloader.....
Info: bootloader version:v2.1.1
Info: wait key input.
Info: User cmd to enter boot.
******Trifo Boot Menu******
1.Modify system parameters
2.Download boot
3.Download app
4.Boot app
5.Exit for reboot
get key input to ota.
Input 3
Info: begin to erase OTA sector.
Info: erase OTA sector finish.
Info: begin to OTA.....
Info: OTA timeout.
```
how to select on the 1 through 5 is via the uart i think, but 'download app/boot' seems to pull from ota (over the air, meaning wifi i think).

if i send 1 over the uart then it gives the next output.

```
/***************************************/
/***********Trifo robotics.*************/
/***************************************/
Info: enter bootloader.....
Info: bootloader version:v2.1.1
Info: wait key input.
Info: User cmd to enter boot.
******Trifo Boot Menu******
1.Modify system parameters
2.Download boot
3.Download app
4.Boot app
5.Exit for reboot
Error: package corrupted.
Error: package corrupted.
Error: package corrupted.
Error: package corrupted.
Error: package corrupted.
Error: package corrupted.
Error: package corrupted.
Error: package corrupted.
Error: package corrupted.
...
```

so i think it expects some form or style of data after the 1 has been read, to set some parameters
