# Setting up a web server: Bash Commands

1. Generate RSA public key
``` bash
ssh-keygen -t rsa -b 4096 
```

2. Generate text for RSA public key
``` bash
cat ~/.ssh/id_rsa.pub 
```

3. copy folder to server
``` bash
scp -r <folder name> root@<Server IP>:/temp
```

4. set up SSH root with IP address
``` bash
ssh root@ <IP Address from Digital Ocean>
```


## Server Commands
1. install firewall on server
``` bash
apt-get -y install firewalld
```

2. set a permanent port for the firewall
``` bash
firewall-cmd --add-port=5001/tcp --permanent
```

3. reload the firewall
``` bash
systemctl reload firewalld
```
