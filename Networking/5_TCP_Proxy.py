# -*- coding: utf-8 -*-
#argv [1] ,[2], [3], [4] ,分別為 外面輸入的指令 1 2 3 4
#EX. python test.py test1 test2 test3 test4 , 會被帶入到程式內
import sys, socket, threading


def server_loop(local_host, local_port, remote_host, remote_port, receive_first):

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

        remote_buffer = receive_from(remote_socket) #先計算出buffer值，透過receive_from函式
        hexdump(remote_buffer) #轉換16進位

        remote_buffer = response_handler(remote_buffer)

        if len(remote_buffer):
            print "[<==] Sending %d bytes to localhost." % len(remote_buffer)
            client_socket.send(remote_buffer)

    #強制做一個while loop
    while True:
        local_buffer = receive_from(client_socket)

        if len(local_buffer):
            print "[==>] Received %d bytes from localhost." %len(local_buffer)
            hexdump(local_buffer)

            local_buffer = request_handler(local_buffer)
            remote_socket.send(local_buffer)
            print "[==>] Send to Remote"

        remote_buffer = receive_from(remote_socket)

        if len(remote_buffer):
            print "[<==] Received %d bytes from remote." %len(remote_buffer)
            hexdump(remote_buffer)

            remote_buffer = response_handler(remote_buffer)

            client_socket.send(remote_buffer)

            print "[<==] Send to localhost"

        if not len(local_buffer) or not len(remote_buffer):
            client_socket.close()
            remote_socket.close()
            print "[*] No more data. Closing connections"
            break



def hexdump(src, length=16):
    result = [] #清掉之前result
    digits = 4 if isinstance(src, unicode) else 2 #如果src是unicode則 digits 為4 ，不然digits為2
    for i in xrange(0, len(src), length):
        s = src[i:i + length]
        hexa = b' '.join(["%0*X" %(digits, ord(x)) for x in s]) #%0*X 寫成bits方式 ，根據digits的數值
        text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        result.append(b"%04X %-*s %s" %(i ,length*(digits + 1), hexa, text))
    print b'\n'.join(result)

def receive_from(connection):
    #清掉之前的buffer
    buffer = ""

    connection.settimeout(2)

    try:
        while True:
            data = connection.recv(4096)

            if not data:
                break

            buffer +=data
    except:
        pass

    return buffer

def request_handler(buffer):
    return buffer

def response_handler(buffer):
    return buffer

main()