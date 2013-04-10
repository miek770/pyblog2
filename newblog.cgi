#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright 2008-2009 Michel Lavoie

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#import cgi
import sys
from time import localtime, strftime
form = cgi.FieldStorage()

urlBlog = '/var/www/blog.html'
urlArchive = '/var/www/archive'
#urlBlog = 'blog.html'
#urlArchive = 'archive'

# get a value from the form
strMessage = str(form.getvalue('message'))
#strMessage = "Message à ajouter... Bon je vais quand même essayer de faire un peu mieux...\nDisons que j'ai été paresseux..."

# print a standard header
#print "Content-Type: text/html"
#print

# print a document
#print "<p>You typed: <tt>%s</tt></p>" % (cgi.escape(strMessage))

# Opens the blog and add the new information
file = open(urlBlog, 'r')
lstBlog = file.readlines()
file.close()

# Inserts the new comment
for i in range(len(lstBlog)):
    if '<!--blog-01-->' in lstBlog[i]:
        lstBlog.insert(i, '<!--blog-01-->\n')
        lstBlog.insert(i+1, '<p>\n<b>[' + strftime("%d %b %Y %H:%M", localtime()) + ' N-Z]</b><br />\n' + strMessage + '\n<br /><i>Mike</i>\n</p>\n')
        break

# Increment the history
booIncrement = False
for i in range(len(lstBlog)):
    if ('<!--blog-01-->' in lstBlog[i]):
        if booIncrement:
            lstBlog.pop(i)
            lstBlog.insert(i, '<!--blog-02-->\n')
            booIncrement = False
            break
        else: booIncrement = True
for i in range(len(lstBlog)):
    if ('<!--blog-02-->' in lstBlog[i]):
        if booIncrement:
            lstBlog.pop(i)
            lstBlog.insert(i, '<!--blog-03-->\n')
            booIncrement = False
            break
        else: booIncrement = True
for i in range(len(lstBlog)):
    if ('<!--blog-03-->' in lstBlog[i]):
        if booIncrement:
            lstBlog.pop(i)
            lstBlog.insert(i, '<!--blog-04-->\n')
            booIncrement = False
            break
        else: booIncrement = True
for i in range(len(lstBlog)):
    if ('<!--blog-04-->' in lstBlog[i]):
        if booIncrement:
            lstBlog.pop(i)
            lstBlog.insert(i, '<!--blog-05-->\n')
            booIncrement = False
            break
        else: booIncrement = True
for i in range(len(lstBlog)):
    if ('<!--blog-05-->' in lstBlog[i]):
        if booIncrement:
            lstBlog.pop(i)
            lstBlog.insert(i, '<!--blog-06-->\n')
            booIncrement = False
            break
        else: booIncrement = True
for i in range(len(lstBlog)):
    if ('<!--blog-06-->' in lstBlog[i]):
        if booIncrement:
            lstBlog.pop(i)
            lstBlog.insert(i, '<!--blog-07-->\n')
            booIncrement = False
            break
        else: booIncrement = True
for i in range(len(lstBlog)):
    if ('<!--blog-07-->' in lstBlog[i]):
        if booIncrement:
            lstBlog.pop(i)
            lstBlog.insert(i, '<!--blog-08-->\n')
            booIncrement = False
            break
        else: booIncrement = True

# Purges the history
booPurgeHistory = False
lstPurges = []
lstArchives = []
for i in range(len(lstBlog)):
    if ('<!--blog-07-->' in lstBlog[i]):
        booPurgeHistory = True
    elif ('<!--blog-08-->' in lstBlog[i]):
        lstPurges.append(i)
        break
    elif booPurgeHistory:
        lstPurges.append(i)
for i in lstPurges:
    lstArchives.append(lstBlog.pop(lstPurges[0]))

# Prints the output for debugging
#for line in lstBlog:
#    print line[:len(line)-1]

# Archives the purged messages
file = open(urlArchive, 'a')
file.seek(0,2)
file.writelines(lstArchives[:len(lstArchives)-1])
file.close()

# Updates the blog
file = open(urlBlog, 'w')
file.writelines(lstBlog)
file.close()
