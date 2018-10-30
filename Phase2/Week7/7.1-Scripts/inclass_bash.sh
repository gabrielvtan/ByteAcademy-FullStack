
# $1 is how we pass arguments to the .sh file
adduser --disabled-password --gecos "" $1

# gives the user super user priveledges
usermod -aG sudo $1

# enter ssh key
mkdir /etc/ssh/$1

# 
mkdir /home/$1/.ssh

# this is how we write lines to nanorc - appends the file
echo "set const" >> .nanorc
echo "set tabsize 4" >> .nanorc
echo "set tabstospaces" >> .nanorc
echo "set autoindent" >> .nanorc
echo "bind ^Z undo main" >> .nanorc

cp .nanorc /home/$1
cp .credentials /home/$1
cat /home/$1/.credentials | chpasswd
rm /home/$1/.credentials
# change ownership of the password folder to the user who created it
chown -R $1:$1 /etc/ssh/$1
# Only user can write to the SSH folder
chmod 755 /etc/shh/$1


