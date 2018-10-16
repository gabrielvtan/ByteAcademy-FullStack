# Setting up a web server: Bash Commands

1. Generate RSA public key
``` bash
ssh-keygen -t rsa -b 4096 
```

2. Generate text for RSA public key
``` bash
cat ~/.ssh/id_rsa.pub 
```

3. set up SSH root with IP address
``` bash
ssh root@ <IP Address from Digital Ocean>
```

