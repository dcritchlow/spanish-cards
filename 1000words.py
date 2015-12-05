#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :1000words.py
#description     :download word and audio for top 1000 spanish words
#author          :Darin Critchlow
#date            :7/10/2015
#=======================================================================
# Import the modules needed to run the script.
from lxml import html
from lxml import etree
import requests, urllib

baseUrl = 'http://wordsgalore.com/wordsgalore/languages/spanish/'
imageURL = 'http://www.google.es/search?site=&tbm=isch&source=hp&biw=1280&bih=642&q='
page = requests.get('http://wordsgalore.com/wordsgalore/languages/spanish/spanish1000.html')
tree = html.fromstring(page.text)

words = tree.xpath('//a/text()')
audios = tree.xpath('//a/@href')
wordsFile = open('spanish_cards.txt', 'w')
# Uncomment lines below to load audio files to "audio/" directory
# for audio in audios[2:]:
#     print audio[3:]
#     urllib.urlretrieve(baseUrl + audio, 'audio/'+audio[3:])

# for word in words:
#   print>>thefile, item

cards = zip(words, audios)

# cardOne = ""
for card in cards[2:]:
    # print>>wordsFile, card[0].encode('utf8')
    line = card[0].encode('utf8')+'<br><br>\t"<img src=""image.jpg"" /><br><br><br><font color=blue>[sound:'+card[1][3:].encode('utf8')+']</font><br><br><br><br><span style=""color:grey""></span><br><br><br><br>"\n"<img src=""image.jpg"" /><br><br><br><br><font color=red></font><br><br><br><font color=red></font><br><br><br>"\t"<span style=""font-size:1.5em;"">'+card[0].encode('utf8')+'</span><br><br><br><br><br><font color=blue>[sound:'+card[1][3:].encode('utf8')+']</font><br><br><br><br><br><span style="""">"'
    print>>wordsFile, line
#     cardOne = card[0]
#     print cardOne
#
# print imageURL + cardOne.replace(' ', '+')
# r = requests.get(imageURL + cardOne.replace(' ', '+'))
# imageTree = html.fromstring(r.text)
# image = imageTree.xpath('//*[@id="rg_s"]/div[1]/a/@href')
# print image
# images = tree.xpath('//*[@id="rg_s"]/div[1]/a/@href')
