#import re
#import mechanize
#import requests
# specify the url
from app_sql import AppSql
from ffjob import FFJob

#from addventure import Episode
#from addventure import Choice
#from create_be_db import AddventureDB
#from bearchive_process import BEarchive_process
#from be_sql_builder import BeSql

sBleachDomain = ''
sInuyDomain = ''
sFateDomain = ''
sGuyverDomain = ''
sDomain = ''
sDomain = ''
sDomain = ''
sDomain = ''
#path = "C:\\G\\IDE\\pycharm\\FFBrowser\\bleach2.db"
#oDB = FanFicDB('test.db')
#oDB.create_db('test.db')
#oDB = FanFicDB(path)
#oDB.create_db(path)
#beDB = AddventureDB('be.db')
#beDB.create_db('be.db')
#sbe = 'http://www.bearchive.com/~addventure/game1/docs/441/441552.html'
#betool = BEarchive_process()
#betool.get_be(sbe)
#sUrl = "https://www.fanfiction.net/anime/Bleach/?&srt=1&r=10" #"https://m.fanfiction.net/anime/Bleach/?srt=1&t=0&g1=0&g2=0&r=10&lan=1&len=5&s=0&c1=0&c2=0&c3=0&c4=0&_g1=0&_c1=0&_c2=0"
#browser.open(quote_page)
#ficList = []
#oIndex = FFNetIndexer('anime/bleach/')
#oIndex.indexFandom()
#quote_page = 'http://tv.adult-fanfiction.org/story.php?no=600092959'
#off = FFNetProcess(path)
#isxover = False
#off.makeIndex("anime/Bleach/", "Bleach", isxover)
settings_db_path = 'appdata.db'
#ffDB = FanFicDB(settings_db_path)
#ffDB.create_settings_db(settings_db_path)
settings = AppSql()
ojob = FFJob()
ojob.create_all_fandoms()
ojob.find_reindex_targets()

#ojob.load_fandom_info()
#ojob.create_index_of_fandoms()

#

                
                    


    
            
    
    


    
    


