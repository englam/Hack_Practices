import socket
import threading

#bind_ip = '0.0.0.0'
ip = '0.0.0.0'
port_number = [20001,30001,40001]


def handle_client(bind_ip,bind_port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((bind_ip, bind_port))
    server.listen(5)
    while True:
        client, addr = server.accept()
        request = client.recv(64)
        print "[*] Received: %s" %request

        client.send("ACK!")
        client.close()



print "[*] Listening on %s:%d" %(ip,port_number[0])

client_handler = threading.Thread(target=handle_client, args=(ip,port_number[0]))
client_handler.start()