# Open ports

shell access on Trifo Max model v1.1 reveals open ports:
- 22 (sshd server, root login with public key in /root/.ssh/authorized_keys)
- 5556 (/userdata/app/bin/calibrate_node process, unknown what this does)
- 7777 (/userdata/app/bin/calibrate_node process, unknown what this does)
- 8554 (/userdata/app/bin/cloudnode process, might be an rtsp stream as suggested by wireshark)
