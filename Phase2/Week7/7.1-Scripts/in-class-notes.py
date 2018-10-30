import os 

email = input('EMAIL = ')
remote_username = input('USERNAME = ')
remote_password = input('PASSWORD = ')
ip_address = input('IP ADDRESS = ')
server_name = input('SERVER NAME = ')
ssh_port = input('NEW SSH PORT = ')

#os_system ("ssh root@{} 'apt-get update'").format(ip_address)

#os.system("ssh root@{} 'apt-get install firewalld nginx fail2ban python3-pip'".format(ip_address))

os.system("rm .credentials")

os.system("echo '{}:{}' >> .credentials".format(remote_username, remote_password))

#TODO copy our credentials file so it actually works

os.system ("ssh root@ {} 'bash -s' < ./inclass_bash.sh {} {}".format(ip_address, remote_username, remote_password))

#TODO configure our installed programs 