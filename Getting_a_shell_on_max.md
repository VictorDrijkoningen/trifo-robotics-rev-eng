# Getting a shell on the Trifo Max (do this on your own risk!)

- Connect to the CPU UART pins on the board. (baudrate 1500000 or 115200)

- Check output is good

- Create an !RSA! ssh key.

```
ssh-keygen -t rsa
```

- Put the contents of the public key that you've just generated into /root/.ssh/authorized_keys

- Do this by spamming a single command like the following into the buggy shell

```
echo "PUBLICKEY" > /root/.ssh/authorized_keys &
```

- Reboot and login via ssh
