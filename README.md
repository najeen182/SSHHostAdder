# SSHHostAdder
Purpose
When you have dozen of server to login on daily basis. Its really difficult typing username and password on each and every server. Another way to reduce is authenticating the server with key basis. But still we need to type the whole server name and port no. Aliases also can be created to reduce minimum typing. But SSH config can do this better. However, adding each host in ssh config can be little hazard. So I came up with idea to add host in ssh config file and copy key to remote server. This tool simple automate manually work that I need to do

Usage
Generate SSH Key
ssh-keygen

Using Application
usage: application.py [-h] -i HOSTNAME [-p CPORT] [-u UNAME] [-c CNAME]

