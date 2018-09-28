import lxml
import requests
import urllib2
import re
import os

from lxml import html
from bs4 import BeautifulSoup

#Set content, which is required in the url:
contentInUrl = ["gauland", "weidel", "poggenburg", "pazderski", "hampel", "von-storch", "driesang", "meuthen"]

#contentnotInUrl = ["/seite/"]
#Extract only those URLs we are interested in:
with open ("urls/afd/afd_2016.txt", "r") as myfile:
    data = myfile.read().split("\n")

#print data

data_correct = []
for dat in data:
    if any(word in dat for word in contentInUrl):
        data_correct.append(dat)
        #print data_correct


seen = set()
result = []
for item in data_correct:
    if item not in seen:
        seen.add(item)
        result.append(item)

#print result

#del result[0]

newfile = open("urls/afd/afd_korrekt_2016.txt", "w")
for ele in result:
    newfile.write(ele+'\n')
newfile.close()


with open ("urls/afd/afd_2017.txt", "r") as myfile:
    data = myfile.read().split("\n")

#print data

data_correct = []
for dat in data:
    if any(word in dat for word in contentInUrl):
        data_correct.append(dat)
        #print data_correct


seen = set()
result = []
for item in data_correct:
    if item not in seen:
        seen.add(item)
        result.append(item)

#print result

#del result[0]

newfile = open("urls/afd/afd_korrekt_2017.txt", "w")
for ele in result:
    newfile.write(ele+'\n')
newfile.close()
