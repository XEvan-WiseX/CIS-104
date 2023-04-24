import urllib.request
import urllib.parse
import urllib.error

link = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
characters = 0
for line in link:
    words = line.decode()
    characters = characters + len(words)
    if characters < 3000:
        print(line.decode().strip())
print('\nCharacter Count: ',characters)