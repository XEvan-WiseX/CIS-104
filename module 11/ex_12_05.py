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
print('\nWebpage Content:\n')
data = skt.recv(512)
header = data.decode()
header_end = header.find('\r\n\r\n') + 4

print(header[header_end:])

while True:
    data = skt.recv(512)
    if len(data) < 1:
        break
    print(data.decode())

skt.close()
    

