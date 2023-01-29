import threading
import socket

def listen(port = 80):
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('0.0.0.0', port))
  server.listen()

  while True:
    client, _ = server.accept()
    thread = threading.Thread(target=handle, args=(client,))
    thread.start()

def write(head, body = ''):
  file = open('server.log', 'a+')
  file.write(getHTTPString(head))
  file.write(str(body))
  file.close()

def handle(client):
  request = str(client.recv(1024).decode('ascii'))
  # write('request', request)

  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(())

  response = getHTTPString('HTTP/1.1 200 OK')
  response += getHTTPString('Content-Type: text/html')
  response += getHTTPString()
  response += getHTTPString(request)
  # write('response', response)

  client.send(response.encode('ascii'))
  client.close()

def getHTTPString(s = ''):
  return str(s + '\r\n')
