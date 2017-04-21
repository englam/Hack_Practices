import socket

target_host = "192.168.13.95"
target_port = 135
i = 0

def run_rang():

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((target_host,target_port))

    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

while True:
    run_rang()
    i+=1
    if i ==100000:
        break
