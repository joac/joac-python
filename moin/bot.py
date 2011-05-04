#!-*- coding:utf8 -*-
import re
import sys
import os

sys.path.insert( 1, '/home/www-pyar/moin/lib/python2.4/site-packages/')
sys.path.append('/home/www-pyar/moin/share/moin/pyar')

from MoinMoin import wikiutil
from MoinMoin.request.request_cli import Request
from MoinMoin.Page import Page
from MoinMoin.PageEditor import PageEditor
from MoinMoin.mail import sendmail

#Path al desposito de Archivos
path ='/home/www-pyar/moin/share/moin/pyar/data/pages'
ignore =[u'ReadWriteGroup',u'AdminGroup',u'BadContent', u'CompilarPython', u'Recetario/EmailConAdjunto']

#Creamos nuestro request de tipo cliente
request = Request()

#Levantamos todas las paginas existentes en el wiki y las convertimos a wikiname
pages = [wikiutil.unquoteWikiname(page) for page in os.listdir(path)]
pages = [page for page in pages if Page(request, page).exists()]

#borramos algunas paginas que no deberian verse
for entry in ignore:
    pages.remove(entry)


#pages = [u'JoaquinSorianello']
mail_dir = re.compile(r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?")
for page in pages:
  #  contents = Page(request, page).get_raw_body()
    
    print Page(request, page).getRevList()
    break
    mails = mail_dir.findall(contents)
    comment = ''
    if contents.find(u'#!python') != -1:
        contents = contents.replace(u'#!python', u'#!code python') 
        comment = u"Fix coloreado"

    if mails:
        # print (u"Los mails para %s son: %s" % (page, ', '.join(mails))).encode('UTF-8')
        for mail in mails:
            contents = contents.replace(mail, u'<<MailTo(%s)>>' % sendmail.encodeSpamSafeEmail(mail))
       # print contents.encode('UTF-8')
        if comment:
            comment += u" y direcciones de mail sin Protecció"
        else:
            comment = u"Fix mail(s) sin protección"
    if comment:
        try:
            PageEditor(request, page).saveText(contents, 0, comment=comment)
            print ("%s: %s" % (page, comment)).encode("UTF-8")
        except :
            print 'Sin Permisos para %s' % page

    if contents.find(u'mailto:') != -1 :
       contents.replace(u'mailto:', '')
       print page.encode('UTF-8'),
