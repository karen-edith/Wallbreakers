import os
import sys
import socket


acceptor = socket.socket() # create a new socket object
acceptor.bind(('localhost', 4232)) # bind socket object to specified address (host and port)
acceptor.listen(6) # listen for connections and limit the number of accepted connections to 6
# all forked children inhert the sockets file descriptor


for i in range(3):
    # create 3 forks (child processes) prior to any connection request
    # returns 0 in the child and returns process id in the parent
    processId = os.fork()

    # when in the child process, get process id
    if processId == 0:
        childProcessId = os.getpid()
        print('child %s accept on on shared socket(localhost:4232)' % childProcessId)

    # when a request connection is received
        try:
            while True:
                # accept the connection and return a pair (connection and requestors address)
                conn, ad = acceptor.accept()
                # recieved data
                data = conn.recv(1024)
                print("child %s echo'd: %r" % (childProcessId, data.decode()))
                # send back same data that was received
                conn.send(data)
        # if connection is interrupted byt ctrl+C exit
        except KeyboardInterrupt:
            sys.exit()
            
# check and wait for the completion of a child process and return a tuple containing
# its process Id and its exit status indication
# if pid equals -1 the request pertains to any child of the current process
try:
    os.waitpid(-1, 0)
# if connection is interrupted byt ctrl+C exit
except KeyboardInterrupt:
    print("\nbailing")
    sys.exit()
