from FFNetProcess import FFNetProcess
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

class FFnetUpdate(FFNetProcess):
    _last_date = ''
    def update_index(self, ffnet_url, fandom_name, isXover):
        oDB = FanFicSql(self._Path)
        #        ffNetFile = open(self._Path, 'a')

        self._is_xover = isXover
        self._Fandom = fandom_name
        oUrl = FanfictionNetUrlBuilder(ffnet_url, "http://", "www.fanfiction.net/")
        # cnt = 810
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
            # time.sleep(6)
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


