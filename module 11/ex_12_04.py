import urllib.request
import urllib.parse
import urllib.error
import ssl
from bs4 import BeautifulSoup


count = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
try:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')


    tags = soup('p')
    for tag in tags:
        count += 1
    print('\nParagraph Count: ',count)

except:
    print('\nCheck Spelling / dependencies')