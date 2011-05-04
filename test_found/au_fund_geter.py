#! -*- coding: utf8 -*-

from BeautifulSoup import BeautifulSoup
import pickle
import urllib
from urlparse import urljoin

url = 'http://www.australianunityinvestments.com.au/FindAFund/Pages/FindAFund.aspx'

def investments_geter(url):
    """Trae una lista con todos los pdfs de una url"""
    page_content = urllib.urlopen(url).read()
    soup = BeautifulSoup(page_content)
    links = soup.findAll('td', {'class':'FundNameCol'})
    links = [urljoin(url, n.a['href']) for n in links if n.nextSibling.string.strip().lower().startswith('equities')]
    return links

def aviso(*args):
    print '%f de %f Kbytes' % (args[0]*args[1] /1024.0, args[2] / 1024.0)

def pdf_geter(url):
    page_content = urllib.urlopen(url).read()
    soup = BeautifulSoup(page_content)
    links = soup.body.div.findAll('ul', {'class':'links'})[0].contents
    link = [ n.a['href'] for n in links if n.a.string.strip().lower().startswith('fund update')]
    if len(link) == 1:
        link = link.pop()
        urllib.urlretrieve(link, filename=link.split('/')[-1], reporthook=aviso )


links = investments_geter(url)
for link in links:
    pdf_geter(link)

# entrar en la url donde estan todos los fondos
# abrir el archivo donde esta pickleada la lista de fondos
# si no existe, crearlo


# scrapear los fondos y descartar los que no sean Equities
# descargar los archivos con nombre "nombrefondo-datetime.pdf"
# crear un diccionario con "nombrefondo":"sha1archivo"
