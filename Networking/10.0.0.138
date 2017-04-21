import socket
import threading

#bind_ip = '0.0.0.0'
bind_ip = '0.0.0.0'
bind_port = raw_input("input bind port: ")
bind_port = int(bind_port)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))


server.listen(5)

print "[*] Listening on %s:%d" %(bind_ip,bind_port)

def handle_client(client_socket):
    request = client_socket.recv(64)
    print "[*] Received: %s" %request

    client_socket.send(request)
    client_socket.close()


client,addr = server.accept()
print "[*] Accepted Connection from: %s:%d" %(addr[0],addr[1])

client_handler = threading.Thread(target=handle_client, args=(client,))
client_handler.start()