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

charcounter = 0

while True:
    data = skt.recv(3000)
    if len(data) < 1:
        break
    print(data.decode(), end=" ")
    for i in data.decode():
        if charcounter >= 3000:
            break
        else:
            charcounter += 1

print('\nCharacters: ', charcounter,)

skt.close()

