import socket, paramiko, threading
import sys

host_key = paramiko.RSAKey(filename='test_rsa.key')

class Server(paramiko.ServerInterface):

    def __init__(self):
        self.event = threading.Event()
    def check_channel_request(self, kind, chanid):
        if kine == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    def check_auth_password(self, username, password):
        if (username == 'englam') and (password == 'englam'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
server = sys.argv[1]
ssh_port = int(sys.argv[2])
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server, ssh_port))
    socket.listen(100)
    print '[+] Listening for connection....'
    client,addr = socket.accept()
except Exception,e:
    print '[-] Listen Failed: ' + str(e)
    sys.exit(1)
print '[+] Got a connection!'

try:
    bhSession = paramiko.Transport(client)
    bhSession.add_server_key(host_key)
    server = server()
    try:
        bhSession.start_server(server=server)
    except paramiko.SSHException, x:
        print '[-] SSH Negotiation Failed.'
    chan = bhSession.accept(20)
    print '[+] Authenticated'
    print chan.recv(1024)
    chan.send('Welcome to Englam SSH Server')
    while True:
        try:
            command = raw_input("Enter Command: ").strip('\n')
            if command != 'exit':
                chan.send(command)
                print chan.recv(1024) + '\n'
            else:
                chan.send('exit')
                print 'Exit'
                bhSession.close()
                raise Exception ('exit')
        except KeyboardInterrupt:
            bhSession.close()
except Exception, e:
    print '[-] Caught exception:' + str(e)
    try:
        bhSession.close()
    except:
        pass
    sys.exit(1)