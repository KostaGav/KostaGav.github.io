import lxml
import requests
import urllib2
import re
import os

from lxml import html
from bs4 import BeautifulSoup

#Set content, which is required in the url:
contentInUrl = ["/content/"]

#contentnotInUrl = ["content", "menu", "footer", "?page=", "field_arbeitsgruppen", "field_topics", "field_abgeordnete"]
#Extract only those URLs we are interested in:
with open ("urls/fdp/fdp.txt", "r") as myfile:
    data = myfile.read().split("\n")

data_correct = []
for dat in data:
    if any(word in dat for word in contentInUrl):
    #if not any(word in dat for word in contentnotInUrl):
        dat = "https://www.liberale.de" + dat
        data_correct.append(dat)


seen = set()
result = []
for item in data_correct:
    if item not in seen:
        seen.add(item)
        result.append(item)

print result

del result[0]

newfile = open("urls/fdp/fdp_korrekt.txt", "w")
for ele in result:
    newfile.write(ele+'\n')
newfile.close()
