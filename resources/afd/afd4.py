from __future__ import with_statement
import urllib2
from bs4 import BeautifulSoup

import urllib2,cookielib
import time
import os, datetime, json
import random
import pandas
import codecs, time



with open ("urls/afd/afd_korrekt_2017.txt", "r") as myfile:
    data = myfile.read().split("\n")

length_data = len(data)
print length_data

count = 0
content_list =[]

output = codecs.open("presse/afd/afd_2017.tsv","a","utf-8")

for count in range(364,length_data-1):
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

    #req = urllib2.Request(web_page, headers={ 'User-Agent': 'Mozilla/57.0' })
    #page = urllib2.urlopen(req)

    content = page.read()

    #print content

    soup = BeautifulSoup(content, "lxml")
    print soup.prettify('utf-8')

    head = soup.findAll("h2", class_="entry-title fusion-post-title") # ("h2")
    for line in head:
        header = line.get_text()
        header = header.replace("\n", " ")
        header = header.replace("\r", " ")
        header = header.replace("\t", " ")
        #print type(header)
        print header

    corp = soup.findAll("div", class_="post-content")  # ("h2")
    for line in corp:
        corpus = line.get_text()
        corpus = corpus.replace("\n", " ")
        corpus = corpus.replace("\r", " ")
        corpus = corpus.replace("\t", " ")
        # print type(header)
        print corpus

    print header

    print count

    output.write("2017" +  "\t" + header + '\t' + corpus + '\n')

    time.sleep(random.randint(1,5))

output.close()



