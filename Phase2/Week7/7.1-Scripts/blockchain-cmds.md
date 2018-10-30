```
wget https://www.multichain.com/download/multichain-1.0.6.tar.gz
tar -xvzf multichain-1.0.6.tar.gz
cd multichain-1.0.6
mv multichaind multichain-cli multichain-util /usr/local/bin
```

tar gz is a type of zip file

command to look in setting of the chain
```
nano ~/.multichain/chain1/params.dat

```

create genesis block/ create blockchain on server 1 - this is the admistrative blockchain server
```
multichaind chain1 -daemon
```

try and connect to node and then ask to be granted permission to connect to the administrative node

log-in in blockchain REPL
```
multichain-cli chain1
```