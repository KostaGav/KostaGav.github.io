import lxml
import requests
import urllib2
import re
import os

from lxml import html
from bs4 import BeautifulSoup

#Erstelle eine Liste an Seiten in den Pressemitteilungen enthalten sind:
count = 0
page_list =[]
url = "http://www.spdfraktion.de/presse/pressemitteilungen?page="
for count in range(1,860):
    page_one = url + str(count)
    page_list.append(page_one)
print page_list


link_list=[]
for p in page_list:
    page = urllib2.urlopen(p)
    soup = BeautifulSoup(page, 'lxml') # 'html.parser')
    links = soup.findAll("a")  # object: single row with all urls of press releases
    #print links # n rows, where n is number of sites containing press releases
#print links

# april 25
    for link in links:
        link_one = link.get("href")
        link_one = unicode(link_one)
        link_one = link_one.encode('utf-8') # decode('iso-8859-1')
#        print link_one  # prints out #rows of links, where #rows = #links; if I write print outside the loop, only last link is printed ("...datenschutz..."
        link_list.append(link_one)
        link_list = filter(None, link_list)  # filters out 'None' entries
    #print link_list  # same content as is print link_one, but single row

#lst = str(lst).encode('utf-8')
newfile = open("urls/spd/spd.txt", "w")
for lst in link_list:
    newfile.write(lst+ '\n')
newfile.close()
