# Trifo Robot Vacuums without an app
~~Trifo Robotics seems to have gone down under.~~ This is my documentation on restoring functionality.
This page is at the moment primarily focused on the Trifo Max model (V1.1). 

Edit: the apps are now working again. This research will still be ongoing to create another way of accessing the device. This could be used to create a homeassistant plugin that controls the robot.

I found [this](https://www.reddit.com/r/RobotVacuums/comments/1d1120l/trifo_robotics_appears_to_have_gone_under_they/) thread after discovery my vaccuum did not have a working app anymore. This started research into accessing the robot software in another way.


# Goal
The main goal of this repo is to ~~restore~~ recreate the functionality the app had in some way (For example planning weekly cleaning sessions etc.)


# Ways of achieving goals:

### Flash dumping
The EMMC chip could be desoldered and read. This could give a readable filesystem where more information could be extracted. Atm this seems the most fruitful.

### SSH server
Somehow finding a shell through the publickey login? 

### ZEROMQ ZMTP
There seems to be some form of an MQTT server running. I am unfamiliar with ZeroMQ ZMTP. Atm i have an client which returns some gibberish i dont understand. This server seems to need a password of some kind
