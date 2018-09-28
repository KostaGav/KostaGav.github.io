from __future__ import with_statement
import urllib2
from bs4 import BeautifulSoup

import urllib2,cookielib
import time
import os, datetime, json

import pandas
import codecs, time



with open ("urls/fdp/fdp_korrekt.txt", "r") as myfile:
    data = myfile.read().split("\n")

length_data = len(data)
print length_data
#length_data_actually = length_data - 2


count = 0
content_list =[]

output = codecs.open("presse/fdp/fdp.tsv","w","utf-8")

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

    meta = soup.findAll("span", class_="date")
    for line in meta:
        if line.parent.name == "article":
            metalvl = line.get_text()
            #print type(metalvl)
            metalvl = metalvl.replace("\n", " ")
            metalvl = metalvl.replace("\t", " ")
            metalvl = metalvl.replace("\r", " ")
            print metalvl

    fraktion = soup.findAll("span", class_="tag", limit=1)
    for line in fraktion:
        if line.parent.name == "article":
            frak = line.get_text()
            print type(frak)
            frak = frak.replace("\n", " ")
            frak = frak.replace("\t", " ")
            frak = frak.replace("\r", " ")
            print frak

    head = soup.findAll("h1") # ("h2")
    for line in head:
        header = line.get_text()
        header = header.replace("\n", " ")
        header = header.replace("\r", " ")
        header = header.replace("\t", " ")
        #print type(header)
        print header

    corpora = ""
    corpus = soup.find("article").findAll("p")
    for corp in corpus:
        corpora += " " + ''.join(corp.findAll(text=True))

    corpora = corpora.replace("\n", " ")
    corpora = corpora.replace("\r", " ")
    corpora = corpora.replace("\t", " ")

    #print frak
    #print metalvl
    #print header
    #print corpora

    output.write(metalvl + "\t" + frak + "\t" + header + '\t' + corpora + '\n')

output.close()



