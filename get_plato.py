import urllib.request
from bs4 import BeautifulSoup
from re import findall
import nltk, re, requests
from nltk import word_tokenize

hdr = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

## get data
def getworksenator(hdr):
    # get names of all works
    all_plato = urllib.request.Request('http://classics.mit.edu/Browse/browse-Plato.html', headers=hdr)
    content = urllib.request.urlopen(all_plato).read()
    soup = BeautifulSoup(content,'html.parser')
    links_to_works = soup.findAll('a', href=True)

    # base site for author
    plato = 'http://classics.mit.edu/Plato/'
    platos = {}

    # create list of sites for all works
    for alink in links_to_works:
        work = findall(r'href="/Plato/(.*?)"',str(alink))
        try:
            platos[work[0]] = plato+work[0]
        except IndexError:
            pass

    # get text from works
    for a_work in platos:
        a_plato = urllib.request.Request(platos[a_work], headers=hdr)
        content = urllib.request.urlopen(a_plato).read()
        soup = BeautifulSoup(content,'html.parser')
        a_text = soup.get_text()
        with open(a_work+'.txt', mode='w') as f:
            f.write(a_text)

if __name__ == '__main__':
    apology = open('apology.html.txt',mode='r').read()

    all_words = word_tokenize(apology)
    print(len(all_words))
