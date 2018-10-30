#Multichain - Tutorial - Setting up Streams
# Set up Multichain on each server:
```
wget https://www.multichain.com/download/multichain-1.0.6.tar.gz -O /tmp/multichain-1.0.6.tar.gz

tar -xvzf multichain-1.0.6.tar.gz -C /opt

cd /opt/multichain-1.0.6/

mv multichain-cli multichaind multichain-util /usr/local/bin
```

#Creating a Blockchain Genesis block - Server1
```
multichain-util create chain1

# View the Blockchain's default settings
cat ~/.multichain/chain1/params.dat

# Initialize the blockchain and create genesis block 
multichaind chain1 -daemon
```

#Connecting to a blockchain - Server2
```
multichaind chain1@<IP Adress>:<Port>
```

#Grant Permission to user to connect to blockchain - Server1
```
multichain-cli chain1 grant 16WVDMbYGhwdvQUeLYEX5ZH6WsoCugC8b5irYt connect
```

# Reconnect with second server - Server2
```
multichaind chain1 -daemon
```

########################################################################
#Create the streams - Server1
```
multichain-cli chain1 create stream pubkeys true
multichain-cli chain1 create stream items true
multichain-cli chain1 create stream access true

# The 'true' values mean the streams are open for writing by any participant who has global send permission on the chain

```
# Publish an RSA key pair - Server1
```
#As a first step, we will generate an RSA public key on the first server, and publish it to the stream for the second server to read.

multichain-cli chain1 listpermissions send
multichain-cli chain1 listaddresses

#An address is suitable if it appears in the output of the first command, and also in the second command together with "ismine" : true
```

```
# Now let’s create a directory for RSA private keys, use openssl to store a new key there

mkdir ~/.multichain/chain1/stream-privkeys/
openssl genpkey -algorithm RSA -out ~/.multichain/chain1/stream-privkeys/1CYomvikpUSkDboWg2kYc6Qt46RVitvf62sYPZ.pem
cat ~/.multichain/chain1/stream-privkeys/1CYomvikpUSkDboWg2kYc6Qt46RVitvf62sYPZ.pem

# The last command creates an RSA private key
```

Now let’s generate a public key from that, convert it immediately to hexadecimal, store it in the pubkeyhex shell variable
```
pubkeyhex=$(openssl rsa -pubout -in ~/.multichain/chain1/stream-privkeys/1CYomvikpUSkDboWg2kYc6Qt46RVitvf62sYPZ.pem | xxd -p -c 9999)
echo $pubkeyhex
```

Finally, let’s publish our public key as an unlabelled item in the pubkeys stream, which should return a transaction ID
```
multichain-cli chain1 publishfrom 1CYomvikpUSkDboWg2kYc6Qt46RVitvf62sYPZ pubkeys '' $pubkeyhex
```

#Store some encrypted data - Server 2
```
# Let's choose an address for posting confidential stream items
multichain-cli chain1 getaddresses
```

# Now use the first server to give global send and receive permissions to this address
```
multichain-cli chain1 grant 16WVDMbYGhwdvQUeLYEX5ZH6WsoCugC8b5irYt send,receive
```

#Create encrypted data
```
#let’s create a random password, use it to encrypt the /proc/cpuinfo operating system file with the AES algorithm, 
convert the result immediately to hexadecimal, store it in the cipherhex shell variable

password=$(openssl rand -base64 48)
cipherhex=$(openssl enc -aes-256-cbc -in /proc/cpuinfo -pass pass:$password | xxd -p -c 99999)
echo $cipherhex
```

Now we can publish this large chunk of hexadecimal data to the items stream
```
multichain-cli chain1 publishfrom 16WVDMbYGhwdvQUeLYEX5ZH6WsoCugC8b5irYt items secret-cpuinfo $cipherhex
```

Now let's create a directory for item passwords, and store this one for future reference
```
mkdir ~/.multichain/chain1/stream-passwords/
echo $password > ~/.multichain/chain1/stream-passwords/c13020efb63fc2f6cebeeb4610a373b4c66be93ea540c6159fde33fff6966a5f.txt
```

# Publish the encrypted Password - Server 2
We need to first subscribe to the pubkeys stream, and then retrieve the first server's RSA public key from that stream
```
multichain-cli chain1 subscribe pubkeys
multichain-cli chain1 liststreampublisheritems pubkeys 1CYomvikpUSkDboWg2kYc6Qt46RVitvf62sYPZ true 1
```

Although the data we need may already be shown in the response, we will retrieve it in a separate step to make it easier to convert from hexadecimal and place in a temporary file, whose contents we can view
```
multichain-cli chain1 gettxoutdata d914e8e722f6e6e9d84b1e7713ae187259732d17f3f8b26fe9ae6903f73bc19c 0 | tail -n 1 | xxd -p -r > /tmp/pubkey.pem
cat /tmp/pubkey.pem

#The output is the RSA public key which was published in the pubkeys stream earlier
```

Now let's use this public key to encrypt the item’s password, convert it immediately to hexadecimal, store it in the keycipherhex shell variable
```
keycipherhex=$(echo $password | openssl rsautl -encrypt -inkey /tmp/pubkey.pem -pubin | xxd -p -c 9999)
echo $keycipherhex
```

Now let’s publish this encrypted password to the access stream, using the previous stream item txid and target address together as a label for the stream item, to enable the other party to easily find it
```
label=c13020efb63fc2f6cebeeb4610a373b4c66be93ea540c6159fde33fff6966a5f-1CYomvikpUSkDboWg2kYc6Qt46RVitvf62sYPZ
multichain-cli chain1 publishfrom 16WVDMbYGhwdvQUeLYEX5ZH6WsoCugC8b5irYt access $label $keycipherhex
```

# Retrieving the Encrypted Item - Server 1
We need to subscribe to the items and access streams, then look for the latest item to be published
```
multichain-cli chain1 subscribe '["items","access"]'
multichain-cli chain1 liststreamitems items true 1
# the txid shown should match the one given from server 2
```

Although the data we need may already be shown in the response, we will retrieve it in a separate step to make it easier to assign to a shell variable:
```
cipherhex=$(multichain-cli chain1 gettxoutdata c13020efb63fc2f6cebeeb4610a373b4c66be93ea540c6159fde33fff6966a5f 0 | tail -n 1)
```

Now let's retrieve the password for this item, which was encrypted especially for this server using its public key
```
label=c13020efb63fc2f6cebeeb4610a373b4c66be93ea540c6159fde33fff6966a5f-1CYomvikpUSkDboWg2kYc6Qt46RVitvf62sYPZ
multichain-cli chain1 liststreamkeyitems access $label true
```

As before, although the data we need may already be shown in the response, we will retrieve it in a separate step:
```
keycipherhex=$(multichain-cli chain1 gettxoutdata 30b5e4cc9ef442e70733abd7c5b8d4f39741ca357f57916e5c1caa004d3a6280 0 | tail -n 1)
```

We can retrieve the original password by decrypting this using the RSA private key stored earlier on this server:
```
password=$(echo $keycipherhex | xxd -p -r | openssl rsautl -decrypt -inkey ~/.multichain/chain1/stream-privkeys/1CYomvikpUSkDboWg2kYc6Qt46RVitvf62sYPZ.pem)
```

And finally we can use this password to decrypt the stream item content, to reveal the secret data that was stored:
```
echo $cipherhex | xxd -p -r | openssl enc -d -aes-256-cbc -pass pass:$password
```