import socket

target_host = "10.0.0.170"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host,target_port))

a=socket.gethostname()

print (a)

client.send("This is Test")

response = client.recv(4096)

print(response)