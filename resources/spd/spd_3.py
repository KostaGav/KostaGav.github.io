from __future__ import with_statement
import urllib2
from bs4 import BeautifulSoup

import urllib2,cookielib
import time
import os, datetime, json

import pandas
import codecs, time



with open ("urls/spd/spd_korrekt.txt", "r") as myfile:
    data = myfile.read().split("\n")

length_data = len(data)
print length_data
#length_data_actually = length_data - 2


count = 0
content_list =[]

output = codecs.open("presse/spd/spd.tsv","w","utf-8")

for count in range(0,length_data-1):
    web_page = data[count]
    web_page = str("http://www.spdfraktion.de") + str(web_page)

    while True:
        try:
            req = urllib2.Request(web_page, headers={'User-Agent': 'Mozilla/57.0'})
            page = urllib2.urlopen(req)
            break
        except urllib2.HTTPError:
            print("Error!!!!")
            continue

    content = page.read()

    #print content

    soup = BeautifulSoup(content, "lxml")
    #print soup

    meta = soup.findAll("dl")
    for line in meta:
        metalvl = line.get_text()
        print type(metalvl)
        metalvl = metalvl.replace("\n", " ")
        metalvl = metalvl.replace("\r", " ")
        metalvl = metalvl.replace("\t", " ")
        print metalvl

    head = soup.findAll("h1") # ("h2")
    for line in head:
        header = line.get_text()
        header = header.replace("\n", "")
        header = header.replace("\r", "")
        header = header.replace("\t", "")
        print type(header)
        print header

    corpus = soup.findAll("div", class_="article-body")
    for corp in corpus:
        text = corp.get_text()
        text = text.replace("\n", "")
        text = text.replace("\r", "")
        text = text.replace("\t", "")
        print text

    #print header
    #print text

    output.write(metalvl + "\t" + header + '\t' + text + '\n')

output.close()


