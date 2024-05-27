# Trifo Robot Vacuums without an app
Trifo Robotics seems to have gone down under. This is my documentation on restoring functionality.
This page is at the moment primarily focused on the Trifo Max model (V1.1).

I found [this](https://www.reddit.com/r/RobotVacuums/comments/1d1120l/trifo_robotics_appears_to_have_gone_under_they/) thread after discovery my vaccuum did not have a working app anymore. This started research into accessing the robot software in another way.

# Goal
The main goal of this repo is to restore the functionality the app had in some way (For example planning weekly cleaning sessions etc.)


# Ways of achieving goals:

### Flash dumping
The EMMC chip could be desoldered and read. This could give a readable filesystem where more information could be extracted.

### SSH server
Somehow finding a shell through the publickey login? 

### The other two unknown open ports
TODO: port detecting to see what services are answering on these ports
