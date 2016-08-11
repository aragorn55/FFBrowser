from bs4 import BeautifulSoup
import os
import time
#import re
#import mechanize
#import requests
from urllib.request import urlopen
from CFanFic import CFanfic
from fanfic import FanFic
from fanfic import Author
from FanfictionNetUrlBuilder import FanfictionNetUrlBuilder
from create_ffbrowse_db import FanFicDB
from fanfic_sql_builder import FanFicSql
# specify the url
import html5lib


class FFNetProcess(object):
    _Path = "ffnetindex.txt"
    _Fandom = ""
    def __init__(self, path):
        self._Path = path

    def makeIndex(self, _FFnetfandom, fandom, isXover):
        self._Fandom = fandom
        oUrl = FanfictionNetUrlBuilder(_FFnetfandom, "http://", "www.fanfiction.net/")
        #cnt = 810
        cnt = 3
        sUrl = oUrl.GenerateUrl(0, 1)
        html = urlopen(sUrl)
        bsObj = BeautifulSoup(html, "html5lib")
        icnt = self.get_fandom_length(bsObj)
        icnt2 = 0
        for x in range(icnt):
            i = x + 1
            sUrl = oUrl.GenerateUrl(0, i)
            try:
                html = urlopen(sUrl)
            except:
                time.sleep(60)
                html = urlopen(sUrl)
            bsObj = BeautifulSoup(html, "html5lib")
            _icnt = self.get_fandom_length(bsObj)
            if _icnt > 0:
                icnt2 = _icnt
            self.processPage(bsObj)
            print(str(i))
            #time.sleep(6)
            time.sleep(5)
        if icnt2 > icnt:
            for a in range(icnt, icnt2):
                ii = a + 1
                sUrl = oUrl.GenerateUrl(0, ii)
                html = urlopen(sUrl)
                bsObj = BeautifulSoup(html, "html5lib")
                self.processPage(bsObj)
                print(str(ii))
                time.sleep(5)


    def process_xover_page(self, vsUrl):
        html = urlopen(vsUrl)
        bsObj = BeautifulSoup(html, "html5lib")
        nameList = bsObj.findAll("div", class_='z-list zhover zpointer ')
        date = ""
        ficList = []
        for x in range(len(nameList)):
            item = nameList[x]
            ofic = self.get_Xover(item)
            ficList.append(ofic)
        self.save_fic_list(ficList)
        return date

    def save_fic_list(self, ficList):
        oDB = FanFicSql(self._Path)
#        ffNetFile = open(self._Path, 'a')
        for x in range(len(ficList)):
            item = ficList[x]
            oDB.save_fic(item)
#            output = item.toFile()
#            ffNetFile.write(output)
#            ffNetFile.write("\r\n")
#        ffNetFile.close()

    def getCharacterListFromString(item):
        charList = item.split(",")
        return charList

    def get_fandom_length(self, bsObj):
        center_element = bsObj.findAll("center")
        ce = center_element[0].findAll("a")
        page_cnt = 0
        for x in range(len(ce)):
            descript = ce[x].get_text()
            if descript == 'Last':
                page_num = ce[x].get('href')
                page_cnt = int(page_num[page_num.find("&p=") + 3:])
                return page_cnt
        return 0

    def processPage(self, bsObj):
        nameList = bsObj.findAll("div", class_='z-list zhover zpointer ')
        date = ""
        ficList = []
        #browser.open(quote_page)

        for x in range(len(nameList)):
            item = nameList[x]
            ofic = CFanfic()
            ofic = self.get_non_Xover(item)
            ficList.append(ofic)

        self.save_fic_list(ficList)
        fic = ficList[len(ficList) - 1]
        test_date = fic.Updated
        if test_date == '':
            date = fic.Published
        else:
            date = fic.Updated

     
        return date

    def get_Xover(self,item):
        ofic = CFanfic()
        href = self.get_href(item)
        ofic.Url = self.get_story_url(href)
        ofic.Title = self.get_title(href)

        print(ofic.Url)
        description = item.findAll("div", class_='z-indent z-padtop')
        descString = self.get_title(description[0])
        ofic.Fandoms = self.get_xoverfandoms(descString)
        ofic.Summary = self.get_summary(descString)
        ofic.Rating = self.get_rating(descString)
        ofic.Genres = self.get_genre(descString)
        ofic.Chapters = self.get_chapters(descString)
        ofic.Words = self.get_words(descString)
        charstring = self.get_characterstring(descString)
        ofic.Characters = self.get_Characters(charstring)
        ofic.Relationships = self.get_RelationShips(charstring)
        ofic.CharactersString = charstring
        meta = item.findAll("div", class_='z-padtop2 xgray')
        metastring = self.get_title(meta[0])
        dates = meta[0].findAll("span")
        if len(dates) > 1:
            date1 = dates[0]
            updated = date1['data-xutime']
            date2 = dates[1]
            published = date2['data-xutime']
            ofic.Published = published
            ofic.Updated = updated
            date = updated
            print(updated)
            print(published)
        else:
            date1 = dates[0]
            published = date1['data-xutime']
            ofic.Published = published
            date = published
            print(published)
        return ofic
    def get_xoverfandoms(self, descString):
        fandomstring = ""
        fandom_list = []
        istart = descString.find("Crossover - ")
        iend = descString.find(" - Rated:")
        fandomstring = descString[istart + 12: iend]
        isplit = fandomstring.count(" & ")
        if isplit > 1:
            fandom_list.append(fandomstring)
        else:
            fandom_list = fandomstring.split(" & ")
        return fandom_list

    def get_non_Xover(self, item):
        descString = ''
        description = ''
        ofic = CFanfic()
        ofic.reset()
        ofic.Author = self.get_author(item)
        href = self.get_href(item)
        ofic.Url = self.get_story_url(href)
        ofic.FFNetID = self.get_ffnet_id(href)
        ofic.Title = self.get_title(href)
        ofic.Fandoms.append(self._Fandom)
        print(ofic.Url)
        description = item.findAll("div", class_='z-indent z-padtop')
        descString = self.get_title(description[0])
        ofic.Summary = self.get_summary(descString)
        ofic.Rating = self.get_rating(descString)
        ofic.Genres.extend(self.get_genre(descString))
        ofic.Chapters = self.get_chapters(descString)
        ofic.Words = self.get_words(descString)
        charstring = self.get_characterstring(descString)
        print(charstring)
        ofic.Characters.extend(self.get_Characters(charstring))
        print(len(ofic.Characters))
        ofic.Relationships.extend(self.get_RelationShips(charstring))
        ofic.CharactersString = charstring
        meta = item.findAll("div", class_='z-padtop2 xgray')
        metastring = self.get_title(meta[0])
        dates = meta[0].findAll("span")
        if len(dates) > 1:
            date1 = dates[0]
            updated = date1['data-xutime']
            date2 = dates[1]

            published = date2['data-xutime']
            ofic.Published = published
            ofic.Updated = updated
            date = updated
            print(updated)
            print(published)
        else:
            date1 = dates[0]
            published = date1['data-xutime']
            ofic.Published = published
            date = published
            print(published)
        return ofic

    def get_title(self, href):
        title = href.get_text()
        return title

    def get_ffnet_id(self, href):
        ffnet = href['href']
        iend = ffnet.find("/", 3)
        fft = ffnet[3:iend]
        print(fft)
        return fft

    def get_story_url(self, href):
        storyurl = "http://www.fanfiction.net"
        storyurl = storyurl + href['href']
        return storyurl

    def get_author(self, item):
        surls = item.findAll("a")
        _author = Author()
        ffneturl = "http://www.fanfiction.net"
        for x in range(len(surls)):
            href = surls[x]
            url = href['href']
            if url.find('/u/') == 0:
                author_list = url.split('/')
                if len(author_list) == 4:
                    #first = author_list[0]
                    #type = author_list[1]
                    ffnetid = author_list[2]
                    a_name = author_list[3]
                    _author.FFNetID = ffnetid
                    _author.AuthorName = a_name
                    _author.Url = ffneturl + url
                elif len(author_list) == 3:
                    ffnetid = author_list[2]
                    _author.FFNetID = ffnetid
                    _author.Url = ffneturl + url
                else:
                    _author.Url = ffneturl + url
                return _author
        _author.FFNetID = '0'
        _author.AuthorID = '0'
        return _author

    def get_href(self, item):
        surl = item.findAll("a", class_='stitle')
        href = surl[0]
        return href

    def get_summary(self, descString):
        rateCnt = descString.find("Rated: ")
        summ = descString[0:rateCnt]
        return summ
    def get_genre(self, descString):
        genrestring = ""
        genre_list = []
        istart = descString.find("English - ")
        iend = descString.find("Chapters:")
        genrestring = descString[istart +10: iend]
        print(genrestring)
        if genrestring.find(" - ") > -1:
            genrestring = genrestring[0:genrestring.find(" - ")]
            if genrestring.find("/") > -1:
                genre_list = genrestring.split("/")
            else:
                genre_list.append(genrestring)
        return genre_list

    def get_rating(self, descString):
        rateCnt = descString.find("Rated: ")
        rate = descString[rateCnt + 7: rateCnt + 8]
        ficRate = ""
        if rate[0:1] == "K":
            if rate[1:2] == "+":
                ficRate = "K+"
            else:
                ficRate = "K"
        elif rate[0:1] == "T":
            ficRate = "T"
        else:
            ficRate = "M"
        return ficRate

    def get_Characters(self, descString):
        if descString.count("[") > 0:
            d = descString.replace('[', ',')
            descString = d.replace(']', ',')
        dd = descString.split(',')
        chars = []
        for item in dd:
            if len(item) > 2:

                item = item.strip()
                print(item)
                chars.append(item)
            elif len(item) == 0 or item.isspace():
               item
            else:
                chars.append(item)
        return chars


    def get_RelationShips(self, descString):
        charstring = ""
        char_strings = []
        rels = []
        relation = []
        front = ''
        back = ''
        leftcnt = descString.count("[")
        for x in range(leftcnt):
            icnt = descString.find("[")
            iend = descString.find("]")
            char_strings.append(descString[:icnt])
            rels.append(descString[icnt:iend])
            descString = descString[iend:]
        for x in range(len(rels)):
            r_string = rels[x]
            r_string = r_string.replace('[', '')
            r_string = r_string.replace(']', '')
            r = self.get_Characters(r_string)
            relation.append(r)
        return relation

    def get_RelationShipsOld(self, descString):
        charstring = ""
        char_strings = []
        rels = []
        relation = []
        front = ''
        leftcnt = descString.count("[")
        for x in range(leftcnt):
            icnt = descString.find("[")
            iend = descString.find("]")
            char_strings.append(descString[:icnt])
            relation.append(descString[icnt:iend])
            descString = descString[iend:]
            re = descString[icnt +1: iend]
            rels.append(re)
            if icnt == 0:
                if iend == len(descString) -1:
                    descString = ""
                else:
                    descString = descString[iend + 1: len(descString) -1]
            else:
                if iend  == len(descString) -1:
                    descString = descString[0:-1]
                else:
                    front = descString[0: icnt -1]
                    end1 = descString[iend + 1:]
                    descString = front + end1
        for x in range(len(rels)):
            r = self.get_Characters(rels[x])
            relation.append(r)
        return relation

    def get_characterstring(self, descString):
        icnt = descString.find("Published: ")
        icnt = descString.find("-", icnt)
        if icnt == -1:
            return ""
        iend = descString.find("- Complete", icnt + 1)
        if iend == -1:
            iend = len(descString)
            characterstring = descString[icnt + 2:]
            return characterstring
        else:
            characterstring = descString[icnt + 2: iend - 1]
            return characterstring


    def get_chapters(self, descString):
        icnt = descString.find("Chapters: ")
        iend = descString.find("-", icnt)
        chapters = descString[icnt + 10: iend - 1]
        chapters = chapters.strip()
        iChap = int(chapters)
        return iChap

    def get_words(self, descString):
        icnt = descString.find("Words: ")
        iend = descString.find("-", icnt)
        words = descString[icnt + 7: iend - 1]
        words = words.strip()
        words = words.replace(',','')
        words = int(words)
        return words
