from __future__ import with_statement
import urllib2
from bs4 import BeautifulSoup

import urllib2,cookielib
import time
import os, datetime, json

import pandas
import codecs, time



with open ("urls/left/left_korrekt.txt", "r") as myfile:
    data = myfile.read().split("\n")

length_data = len(data)
print length_data
#length_data_actually = length_data - 2


count = 0
content_list =[]

output = codecs.open("presse/left/left.tsv","w","utf-8")

for count in range(0,length_data-1):
    web_page = data[count]
    print web_page

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

    meta = soup.findAll("span", class_="news-list-date")
    for line in meta:
        metalvl = line.get_text()
            #print type(metalvl)
        metalvl = metalvl.replace("\n", " ")
        metalvl = metalvl.replace("\r", " ")
        metalvl = metalvl.replace("\t", " ")
        #print metalvl

    head = soup.findAll("div", class_="header white") # ("h2")
    for line in head:
        header = line.get_text()
        header = header.replace("\n", " ")
        header = header.replace("\r", " ")
        header = header.replace("\t", " ")
        #print type(header)
        #print header

    corp = soup.findAll("div", class_="news-text-wrap") # ("h2")
    print corp
    for line in corp:
        corpus = line.get_text()
        corpus = corpus.replace("\n", " ")
        corpus = corpus.replace("\r", " ")
        corpus = corpus.replace("\t", " ")
        #print type(header)
        #print corpus

    print metalvl
    print header
    print corpus

    output.write(metalvl +  "\t" + header + '\t' + corpus + '\n')

output.close()



