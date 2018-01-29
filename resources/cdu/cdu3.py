from __future__ import with_statement
import urllib2
from bs4 import BeautifulSoup

import urllib2,cookielib
import time
import os, datetime, json
import random
import pandas
import codecs, time



with open ("urls/cdu/cdu_korrekt_pm.txt", "r") as myfile:
    data = myfile.read().split("\n")

length_data = len(data)
print length_data
#length_data_actually = length_data - 2


count = 0
content_list =[]

output = codecs.open("presse/cdu/cdu.tsv","a","utf-8")

for count in range(5896,length_data-1):
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

    soup = BeautifulSoup(content, "lxml",from_encoding='utf-8')
    print soup.prettify('utf-8')

    meta = soup.findAll("span", class_="meta-tag press")
    for line in meta:
        metalvl = line.get_text()
            #print type(metalvl)
        metalvl = metalvl.replace("\n", " ")
        metalvl = metalvl.replace("\r", " ")
        metalvl = metalvl.replace("\t", " ")
        print metalvl

    head = soup.findAll("h1") # ("h2")
    for line in head:
        header = line.get_text()
        header = header.replace("\n", " ")
        header = header.replace("\r", " ")
        header = header.replace("\t", " ")
        #print type(header)
        print header

    corp1 = soup.findAll("h2")  # ("h2")
    for line in corp1:
        corpus1 = line.get_text()
        corpus1 = corpus1.replace("\n", " ")
        corpus1 = corpus1.replace("\r", " ")
        corpus1 = corpus1.replace("\t", " ")
        # print type(header)
        print corpus1

    corp2 = soup.findAll("strong", class_="subtitle")  # ("h2")
    for line in corp2:
        corpus2 = line.get_text()
        corpus2 = corpus2.replace("\n", " ")
        corpus2 = corpus2.replace("\r", " ")
        corpus2 = corpus2.replace("\t", " ")
        # print type(header)
        print corpus2

    corp3 = soup.findAll("div", class_="wysiwyg-wrapper")  # ("h2")
    for line in corp3:
        corpus3 = line.get_text()
        corpus3 = corpus3.replace("\n", " ")
        corpus3 = corpus3.replace("\r", " ")
        corpus3 = corpus3.replace("\t", " ")
        # print type(header)
        print corpus3

    print metalvl
    print header
    corpus = corpus1 + corpus2 + corpus3

    print count

    output.write(metalvl +  "\t" + header + '\t' + corpus + '\n')

    time.sleep(random.randint(1,5))

output.close()



