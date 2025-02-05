import threading
import socket

host = '127.0.0.1' # localhost
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# send a message to all of the clients connected
def broadcast(message):
  for client in clients:
    client.send(message)

# handle a connection to a user
def handle(client):
  while True:
    try:
      message = client.recv(1024) # 1024 bytes
      broadcast(message)
    except:
      # client is no longer connected
      index = clients.index(client)
      clients.remove(client)
      client.close()
      nickname = nicknames[index]
      broadcast(f'{nickname} salio del chat\n'.encode('ascii'))
      nicknames.remove(nickname)
      break

def receive():
  while True:
    # listening for connecting clients
    client, address = server.accept()
    print(f'Conectado con {str(address)}')

    # ask for the nickname
    client.send('NICK'.encode('ascii'))
    nickname = client.recv(1024).decode('ascii')
    nicknames.append(nickname)
    clients.append(client)

    # broadcast when someone connects
    print(f'Nickname del cliente es: {nickname}')
    broadcast(f'{nickname} ha entrado al chat.'.encode('ascii'))
    client.send('Conectado al servidor!'.encode('ascii'))

    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

print('El servidor esta escuchando...')
receive()
