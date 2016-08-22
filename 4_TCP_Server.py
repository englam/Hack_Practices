# -*- coding: utf-8 -*-
#opts, args = getopt,getopt(sys.argv[1:], 'ho:', ['help', 'output='])

#sys.argv[1:]   ----------------過瀘掉第一個參數, 因為第一個參數要用 test.py or other

#短格式顯示方式：
#'ho:'          ---------------- h 為一個選項開關 , o: 因為有分號所以o後面必需帶一個參數， 如果此例為h:o:則 h and o後面都要帶參數

#長格式顯示方式：
#['help', 'output="'] ----------- 'help' 為一個選項開關, 'output=' 後面必需帶一個參數

#上例opts格式應為 [('-h',''),('-c','file'),('--help',''),('--output','out')]
#   args格式應為 ['file1' , 'file2']
import sys, socket, getopt, threading, subprocess

listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0

def usage():
    print "Englam Net Tool"
    print
    print "Usage: 4_TCP_Server.py -t target_host -p port"
    print "-l --listen              -[host]:[port] listening connection"
    print "-e --execute=file_to_run -executing file after connection established"
    print "-c --command             -start shell"
    print "-u --upload=destination  -upload file and print destination after connection established"
    print
    print
    print "example: "
    print "4_TCP_Server.py -t 192.168.0.1 -p 5555 -l -c"
    print "4_TCP_Server.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "4_TCP_Server.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo 'ABCDEFGHI' | ./4_TCP_Server.py -t 192.168.11.12 -p 135"
    sys.exit(0)

def main():
    global listen
    global port
    global execute
    global command
    global upload_destination
    global target

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:", ["help","listen","execute","target","port","command","upload"])
    except getopt.GetoptError as error:
        print str(error)
        usage()

# opts內容包含 選項 跟 參數, o指定為選項, a指定為參數
    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = True
        elif o in ("-e", "--execute"):
            execute =a
        elif o in ("-c", "--commandshell"):
            command = True
        elif o in ("-u", "--upload"):
            upload_destination = a
        elif o in ("-t", "--target"):
            target = a
        elif o in ("-p", "--port"):
            port = int(a)
        else:
            assert False, "option does not disposal"

    if not listen and len(target) and port > 0:
        #sys.stdin.read()讀取全部的參數, sys.stdin.read(1)讀取第一個數值
        buffer = sys.stdin.read()

        client_sender(buffer)

    if listen:
        server_loop()


def client_sender(buffer):
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    try:
        client.connect((target,port))

        if len(buffer):
            client.send(buffer)

        while True:

            recv_len = 1
            response = ""

            while recv_len:

                data = client.recv(4096)
                recv_len = len(data)
                response+=data

            print response,

            buffer = raw_input("")
            buffer += "\n"

            client.send(buffer)

    except:
        print "[*] Exception Exiiting."
        client.close()

def server_loop():
    global target

    if not len(target):
        target = "0.0.0.0"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((target,port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()

        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()

def run_command(command):
    command = command.rstrip()

    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except:
        output = "執行失敗. \r\n"

    return output

def client_handler(client_socket):
    global upload
    global execute
    global command

    #如果我有輸入upload_destination的話 才執行下面的程式
    if len(upload_destination):

        file_buffer =""

        while True:
            data = client_socket.recv(1024)

            if not data:
                break
            else:
                file_buffer += data

        try:
            file_description = open(upload_destination, "wb")
            file_description.write(file_buffer)
            file_description.close()

            client_socket.send("Successfully saved file to %s \r\n" %upload_destination)
        except:
            client_socket.send("Failed to save file to %s\r\n" %upload_destination)

    #如果我有輸入execute的話 才執行下面的程式
    if len(execute):
        output = run_command(execute)

        client_socket.send(output)

    if command:
        while True:
            client_socket.send("<BHP:#> ")

            cmd_buffer = ""

        while "\n" not in cmd_buffer:
            cmd_buffer += client_socket.recv(1024)

        response = run_command(cmd_buffer)

        client_socket.send(response)

main()