from bs4 import BeautifulSoup
#import re
#import mechanize
#import requests
from urllib.request import urlopen
# specify the url
from CFanFic import CFanfic
from FFNetProcess import FFNetProcess
from create_ffbrowse_db import FanFicDB

path = "C:\\G\\IDE\\pycharm\\FFBrowser\\ffbrowse.db"
oDB = FanFicDB('ffbrowse.db')
oDB.create_db('ffbrowse.db')
#sUrl = "https://www.fanfiction.net/anime/Bleach/?&srt=1&r=10" #"https://m.fanfiction.net/anime/Bleach/?srt=1&t=0&g1=0&g2=0&r=10&lan=1&len=5&s=0&c1=0&c2=0&c3=0&c4=0&_g1=0&_c1=0&_c2=0"
#browser.open(quote_page)
#ficList = []
#oIndex = FFNetIndexer('anime/bleach/')
#oIndex.indexFandom()
#quote_page = 'http://tv.adult-fanfiction.org/story.php?no=600092959'
off = FFNetProcess(path)
off.makeIndex("anime/Bleach/", "Bleach")



                
                    


    
            
    
    


    
    


