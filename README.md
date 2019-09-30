# reverse-shell-python

I implemented this project to gain experience in TCP/IP programming. In this project, the client.py file connects to the remote server.py
file which I installed on an AWS EC2 Server. Once the two files are connected through TCP, the server will send commands (inputted by the
user) for the client to execute. Once the client executes the appropriate commands sent by the user, it will send the output in the shell
back to the server.
