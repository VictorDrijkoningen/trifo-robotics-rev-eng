# Wireshark
(ip.src==robotip or ip.dst==robotip) and not ip.dst==255.255.255.255
When on the same network as a Trifo max, wireshark captures a packet sent to the whole network. This contains a string of data with robotname - macadress

