#Droplet Checklist

- Start up nation
- zero to one mk
- the right kind of crazy 
- the medicci effect 

#Books 
- design patterns gang of four
- the art of computer programming
- the catheedral and the bizare 

# Read 
- untangling the web
-   ssh-keygen -t rsa -b 4096
-hash = hashlib.sha256(b'a').hexdigest()
- hexadecimal
- inhernt and defend excercise

- Click an image/Choose an os image  
- 142.93.64.34 - privat IP adress for digital 
- scp -r Desktop/Byte/Course_Work/Phase2/D2/web_trader root@142.93.64.34:/tmp -  this is how to copy the files onto the server

- read about the fhs, linux file hierarchy system 
- katabasis - github for bash commands 
- man cmd
- Chromanslack

- ssh root@142.93.64.34

#Bash Commands

apt - its bascially the brew but for the server

htop - shows a high level overview of what processes are happineing 

iotop -o - what is being read in and out of the disk that is not a kernal process

sudo - is used access root user privelages 

iftop - shows all the process running on the wifi 

sudo iftop -i wlsp30

slurm -s -i eth0 - the shape of your traffic, the flatter the red and green line, the faltter the traffic

curl http://icanhazip.com - tells you your ip address

glances - another one that shows process

apt-get -y install firewalld - the -y forces the yes

systemctl status firewalld - system controll status then name of module

daemon - means background process

firewall-cmd --list-all - shows you the zone 

firewall-cmd --add-port=5000/tcp --permanent - lets the port pass the firewall

systemctl reload firewalld  
ystemctl status firewalld  
ystemctl start firewalld  
ystemctl enable firewalld  - entire firewalld well start next time the whole computer starts 