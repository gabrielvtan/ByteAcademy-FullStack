#3 - Some commands in Interactive Mode
Enter the REPL
```
multichain-cli chain1
```
Basic Commands
```
getinfo
help
listpermissions
getnewaddress #create new address in wallet
getblockchainparams
getpeerinfo
```
#4 - Streams
Now let’s create a stream, which can be used for general data storage and retrieval. On the first server:
```
create stream stream1 false
# false means the stream can only be written to by those with explicit permissions
```
