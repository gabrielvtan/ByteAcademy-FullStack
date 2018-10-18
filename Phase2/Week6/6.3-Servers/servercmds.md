#Server Commands
Update the package manager - do this every time you create a new server
```bash
apt-get -y update
```

Install the following deployment modules
fail2ban - instrusion dectection system
firewalld - software firewall
nginx - reverse proxy - also http web server
ntp - network time protocol 
```bash
apt-get -y install fail2ban firewalld nginx ntp python3-pip
```

Check the status of the each of the modules
```bash
systemctl status fail2ban firewalld nginx ntp python3-pip
```

Modify SSH daemon
```bash
nano /etc/ssh/sshd_config
```

skel is a folder for the newly created users

history of your server commands
```bash
journalctl -xe
```