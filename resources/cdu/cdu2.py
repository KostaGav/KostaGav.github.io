import lxml
import requests
import urllib2
import re
import os

from lxml import html
from bs4 import BeautifulSoup

#Set content, which is required in the url:
contentInUrl = ["presse/pressemitteilungen"]

#contentnotInUrl = ["/seite/"]
#Extract only those URLs we are interested in:
with open ("urls/cdu/cdu.txt", "r") as myfile:
    data = myfile.read().split("\n")

#print data

data_correct = []
for dat in data:
    if any(word in dat for word in contentInUrl):
        dat = "https://www.cducsu.de/" + dat
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

newfile = open("urls/cdu/cdu_korrekt_pm.txt", "w")
for ele in result:
    newfile.write(ele+'\n')
newfile.close()
