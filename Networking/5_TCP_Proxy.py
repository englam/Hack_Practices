# -*- coding: utf-8 -*-
#argv [1] ,[2], [3], [4] ,分別為 外面輸入的指令 1 2 3 4
#EX. python test.py test1 test2 test3 test4 , 會被帶入到程式內
import sys, socket, threading

def server_loop(local_host, local_port, remote_host, remote_port, receive_first):

    server = socket.socket.(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind((local_host,local_port))
    except:
        print "[!!] Failed to listen on %s:%d" %(local_host,local_port)
        print "[!!] Check for other listening sockets or correct permissions."
        sys.exit(0)

    print "[*] Listening on %s:%d" %(local_host,local_port)

    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        print "[==>] Received incoming connection from %s:$d" %(addr[0],addr[1])

        proxy_thread = threading.Thread(target=proxy_handler, args=(client_socket, remote_host, remote_port, receive_first))

        proxy_thread.start()


def main():
    if len(sys.argv[1:]) != 5:
        print "Usage: ./proxy.py [localhost] [localport] [remotehost] [remoteport] [receive_first]"
        print "Example : ./proxy.py 127.0.0.1 9000 10.12.132.1 9000 True"
        sys.exit(0)

    local_host = sys.argv[1]
    local_port = int(sys.argv[2])

    remote_host = sys.argv[3]
    remote_port = int(sys.argv[4])

    receive_first = sys.argv[5]

    if "True" in receive_first:
        receive_first = True
    else:
        receive_first = False

    server_loop(local_host, local_port, remote_host, remote_port , receive_first)


def proxy_handler(client_socket, remote_host, remote_port, receive_first):

    remote_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    remote_socket.connect((remote_host,remoteport))

    if receive_first:

        remote_buffer = receive_from(remote_socket)
        hexdump(remote_buffer)

        remote_buffer = response_handler(remote_buffer)

        if len(remote_buffer):
            print "[<==] Sending %d bytes to localhost." % len(remote_buffer)
            client_socket.send(remote_buffer)


main()