import socket
import threading

nickname = input('Ingresa tu nickname: ')

# conect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

def receive():
  while True:
    try: 
      message = client.recv(1024).decode('ascii')
      if message == "NICK":
        client.send(nickname.encode('ascii'))
      else:
        print(message)
    except Exception as e:
      print(f'Un error ha ocurrido! {e}')
      client.close()
      break

def write():
  while True:
    message = f'{nickname}: {input()}'
    client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()