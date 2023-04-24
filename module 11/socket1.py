import socket

skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    location = input('Enter URL:')
    site = location.split('/')
    host = site[2]
    skt.connect((host, 80))
    cmd = 'GET '.encode() + location.encode() + ' HTTP/1.0\r\n\r\n'.encode()
except IndexError:
    print('Invalid Address')
    print(site)
    quit()

skt.send(cmd)

while True:
    data = skt.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end=" ")

skt.close()

