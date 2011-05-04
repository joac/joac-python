#!-*- coding:utf8 -*-
import random
import os
import sys
import pygraphviz as gv
from MoinMoin import wikiutil, user
from MoinMoin.request.request_cli import Request
from MoinMoin.Page import Page

def int2hex_color(number):
    hexa = hex(number)[2:8]
    print hexa
    longitud = len(hexa)
    if  longitud < 6:
        hexa = ('0'*(6-longitud))+hexa
    print hexa  
    return '#'+hexa

#Agregamos el path al wikiconfig.py de pyar
sys.path.append('/home/www-pyar/moin/share/moin/pyar')

#Path al desposito de Archivos
path ='/home/www-pyar/moin/share/moin/pyar/data/pages'
ignore =[u'ReadWriteGroup',u'AdminGroup',u'BadContent']

#Creamos nuestro request de tipo cliente
request = Request()

#Levantamos todas las paginas existentes en el wiki y las convertimos a wikiname
pages = [wikiutil.unquoteWikiname(page) for page in os.listdir(path)]
pages = [page for page in pages if Page(request, page).exists()]

#borramos algunas paginas que no deberian verse
for entry in ignore:
    pages.remove(entry)

#Iniciamos el Grafico
graph = gv.AGraph(directed=True, splines="true", )

print "Rellenando nodos"
for page in pages:
    page_utf8 = page.encode('utf8')
    graph.add_node(page_utf8, shape ='plaintext', href="http://python.org.ar/pyar/"+page_utf8, tooltip = "Click para ir a la página")
    print '.',    
for page in pages:
    links = Page(request, page).getPageLinks(request)
    page = page.encode("utf8")
    color = random.randint(0, 0xffffff)    
    for link in links:
        if link in pages:
            link = link.encode("utf8")
            graph.add_edge(page, link, color=int2hex_color(color))
    print '.',
    
print "Generando Grafico"
graph.draw("grafo.svg", prog='fdp')


