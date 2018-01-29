import lxml
import requests
import urllib2
import re
import os

from lxml import html
from bs4 import BeautifulSoup

#Erstelle eine Liste an Seiten in den Pressemitteilungen enthalten sind:
count = 0
page_list1 =[]
page_list2 =[]
url1 = "https://www.afd.de/2016/page/"
url2 = "https://www.afd.de/2017/page/"
for count in range(0,39):
    page_one = url1 + str(count)
    page_list1.append(page_one)
print page_list1
for count in range(0,64):
    page_one = url2 + str(count)
    page_list2.append(page_one)
print page_list2




link_list=[]
for p in page_list1:
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
newfile = open("urls/afd/afd_2016.txt", "a")
for lst in link_list:
    newfile.write(lst+ '\n')
newfile.close()



link_list=[]
for p in page_list2:
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
newfile = open("urls/afd/afd_2017.txt", "a")
for lst in link_list:
    newfile.write(lst+ '\n')
newfile.close()
