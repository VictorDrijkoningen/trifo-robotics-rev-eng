# Open ports

nmap scan of Trifo Max model v1.1 reveals open ports:
- 22
- 5556
- 7777

port 22 is confirmed to be an ssh server, as login creates an access denied as an ssh would.


```nmap -p1-65000 -sV --version-intensity 9 ROBOTIP```
Reveals very interesting results:
```
22/tcp   open  ssh     OpenSSH 7.6 (protocol 2.0)
5556/tcp open  zmtp    ZeroMQ ZMTP 2.0
7777/tcp open  zmtp    ZeroMQ ZMTP 2.0
```

Wireshark revealed rtsp on port 8554

