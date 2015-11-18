#-*- coding : utf-8 -*-
import urllib
import requests
import sys
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("shift-jis")

version = input("VERSION : ")
lev_input = input("LEVEL : ")

version = int(version)
lev_input = int(lev_input)


print version
print lev_input

if version == 2:
    url = "http://p.eagate.573.jp/game/sdvx/ii/p/music/detail.html?list_id="
    for i in range(1,47 +1):
        req = requests.get(url+str(i))
        soup = BeautifulSoup(req.text.encode("shift-jis","ignore"))
        song_info = soup.findAll("ul", {"class" : "databox"})
        for j in range(0, len(song_info)):
            exh = song_info[j].select("li")[2]
            level = exh.find("div", {"class" : "exh"}).string
            if int(level) == lev_input:
                print level
                album_img = exh.select("img")[0]['src']
                urllib.urlretrieve("http://p.eagate.573.jp" + album_img, str(i) + "_" +  str(j) + ".png")
                print (str(i) + "_" +  str(j) + ".png")
        
                try:
                    grv = song_info[j].select("li")[3]
                    level = grv.find("div", {"class" : "inf"}).string
                    print ("INF!")
                    if level == lev_input:
                        album_img = grv.select("img")[0]['src']
                        urllib.urlretrieve("http://p.eagate.573.jp" + album_img, str(i) + "_" +  str(j) + ".png")
                        print (str(i) + "_" +  str(j) + ".png")
                except:
                    print ("no INF")

elif version == 3:
    url = "http://p.eagate.573.jp/game/sdvx/iii/p/music/detail.html?list_id="
    for i in range(1,36+1):
        req = requests.get(url+str(i))
        soup = BeautifulSoup(req.text.encode("shift-jis","ignore"))
        song_info = soup.findAll("ul", {"class" : "databox"})
        for j in range(0, len(song_info)):
            exh = song_info[j].select("li")[2]
            level = exh.find("div", {"class" : "exh"}).string
            if int(level) == lev_input:
                album_img = exh.select("img")[0]['src']
                urllib.urlretrieve("http://p.eagate.573.jp" + album_img, str(i) + "_" +  str(j) + ".png")
                print (str(i) + "_" +  str(j) + ".png")

                try:
                    grv = song_info[j].select("li")[3]
                    level = grv.find("div", {"class" : "grv"}).string
                    print ("GRV!")
                    if level == lev_input:
                        album_img = grv.select("img")[0]['src']
                        urllib.urlretrieve("http://p.eagate.573.jp" + album_img, str(i) + "_" +  str(j) + ".png")
                        print (str(i) + "_" +  str(j) + ".png")
                except:
                    print ("no GRV")    
