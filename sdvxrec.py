#!/usr/bin/python
#-*- coding : utf-8 -*-
import urllib
import requests
import sys
import random
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("shift-jis")

def get_song(lev = None, sdvx_ver = None) :
    print "received level is " + str(lev)
    print "received version is " + str(sdvx_ver)
    if sdvx_ver == None:
        sdvx_ver = random.randint(2,3)
    elif int(sdvx_ver) > 4 :
        return {'sdvx_ver' : 0, 'page' : 0 , 'idx' : 0, 'error' : 'Version' }
    
    if lev == None:
        return {'sdvx_ver' : 0, 'page' : 0 , 'idx' : 0, 'error' : 'Level' }

    lev = int(lev)
    sdvx_ver = int(sdvx_ver)

    if lev == 16 and sdvx_ver == 3:
        songArr = [
            {'sdvx_ver' : sdvx_ver, 'page' : 15 , 'idx' : 0, "title" : "KAC 2012 ULTIMATE MEDLEY -HISTORIA SOUND VOLTEX-" },
            {'sdvx_ver' : sdvx_ver, 'page' : 16 , 'idx' : 4, "title" : "Everlasting Message" },
            {'sdvx_ver' : sdvx_ver, 'page' : 30 , 'idx' : 0, "title" : "A" },
            {'sdvx_ver' : sdvx_ver, 'page' : 30 , 'idx' : 1, "title" : "Blastix Riotz" },
            {'sdvx_ver' : sdvx_ver, 'page' : 30 , 'idx' : 2, "title" : "Preserved Valkyria" },
            {'sdvx_ver' : sdvx_ver, 'page' : 30 , 'idx' : 3, "title" : "XyHATTE" },
        ]
        return random.choice(songArr)
    elif lev == 16 and sdvx_ver == 2:
        songArr = [
            {'sdvx_ver' : sdvx_ver, 'page' : 21 , 'idx' : 0, "title" : "For UltraPlayers" },
            {'sdvx_ver' : sdvx_ver, 'page' : 21 , 'idx' : 1, "title" : "Bangin' Burst" },
        ]        
        return random.choice(songArr)

    page = 0
    url = ""
    selected_page = 1
    b_page = 0
    b_idx = 0
    if sdvx_ver == 2 :
        page = 47
        url = "http://p.eagate.573.jp/game/sdvx/ii/p/music/detail.html?list_id="
        print "sdvx version is 2"
    elif sdvx_ver == 3 :
        page = 36
        url = "http://p.eagate.573.jp/game/sdvx/iii/p/music/detail.html?list_id="
        print "sdvx version is 3"
    print "page is " + str(page)
    selected_page = random.randint(1,page)
    print "selected page is " + str(selected_page)
    
    req = requests.get(url+str(selected_page))
    #soup = BeautifulSoup(req.text.decode("UTF-8").encode("shift-jis", "ignore"))
    soup = BeautifulSoup(req.text.encode("shift-jis"))
    song_info = soup.findAll("ul", {"class" : "databox"})
    title = soup.findAll("div", {"class" : "title_text"})
    selected_song = random.randint(0,len(song_info)-1)
    diff_flag = random.randint(0,1)
    if (diff_flag == 0):
        exh = song_info[selected_song].select("li")[2]
        level = exh.find("div", {"class" : "exh"}).string
    else :
        try :
            grv = song_info[selected_song].select("li")[2]
            level = grv.find("div", {"class" : "grv"}).string
        except :
            return get_song(lev, sdvx_ver)
    print "-----------------------------------------------------"
    print "Founded Level is " + str(level)
    print "User requested level is " + str(lev)
    print "User requested level is " + str(sdvx_ver)
    print title[selected_song].string
    print "-----------------------------------------------------"
        
    if (selected_page == b_page and selected_song == b_idx):
        print "Same song!"
        return get_song(lev, sdvx_ver)

    elif int(level) == int(lev):
        print lev
        print title[selected_song].string
        return {'sdvx_ver' : sdvx_ver, 'page' : selected_page , 'idx' : selected_song, "title" : title[selected_song].string }
        b_page = selected_page
        b_idx = selected_song
        #return str(title[selected_song].string)
    else:
        return get_song(lev, sdvx_ver)
