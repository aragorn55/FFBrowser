# import re
# import mechanize
# import requests
# specify the url
from ffjob import FFJob

# from addventure import Episode
# from addventure import Choice
# from create_be_db import AddventureDB
# from bearchive_process import BEarchive_process
# from be_sql_builder import BeSql


# path = "C:\\G\\IDE\\pycharm\\FFBrowser\\bleach2.db"
# oDB = FanFicDB('test.db')
# oDB.create_db('test.db')
# oDB = FanFicDB(path)
# oDB.create_db(path)
# beDB = AddventureDB('be.db')
# beDB.create_db('be.db')
# sbe = 'http://www.bearchive.com/~addventure/game1/docs/441/441552.html'
# betool = BEarchive_process()
# betool.get_be(sbe)
# sUrl = "https://www.fanfiction.net/anime/Bleach/?&srt=1&r=10"
# #"https://m.fanfiction.net/anime/Bleach/?srt=1&t=0&g1=0&g2=0&r=10&lan=1&len=5&s=0&c1=0&c2=0&c3=0&c4=0&_g1=0&_c1=0&_c2=0"
# browser.open(quote_page)
# ficList = []
# oIndex = FFNetIndexer('anime/bleach/')
# oIndex.indexFandom()
# quote_page = 'http://tv.adult-fanfiction.org/story.php?no=600092959'
# off = FFNetProcess(path)
# isxover = False
# off.makeIndex("anime/Bleach/", "Bleach", isxover)
# settings_db_path = 'appdata.db'
# ffDB = FanFicDB(settings_db_path)
# ffDB.create_settings_db(settings_db_path)
# settings = AppSql()
ojob = FFJob()
# ojob.create_all_fandoms()
ojob.remove_dup_fics_from_all()
# ojob.reindex_fandom_by_id(2)
# ojob.reindex_fandom_by_id(24)
# ojob.reindex_fandom_by_id(22)
# ojob.reindex_fandom_by_id(26)
# ojob.reindex_fandom_by_id(13)
# ojob.reindex_fandom_by_id(16)
# ojob.reindex_fandom_by_id(23)

# ojob.reindex_fandom_by_id()
# ojob.test()
# ojob.find_reindex_targets()
# targets = ojob.get_reindex_targets()
# for item in targets:
#     print('fandom_id' + str(item.FandomId))
#     print('fandom_url' + item.FandomUrl)
#ojob.update_index_of_fandoms()
# ojob.create_all_fandoms()
# ojob.reindex_fandom_by_id(2)
# ojob.reindex_fandom_by_id(24)
# ojob.reindex_fandom_by_id(22)
# ojob.reindex_fandom_by_id(26)
# ojob.reindex_fandom_by_id(13)
# ojob.reindex_fandom_by_id(16)
#ojob.reindex_fandom_by_id(23, 0)
#ojob.get_reindex_targets()
#ojob.create_ficlink_db()
#ojob.add_all_fandoms_to_link_list()
#ojob.add_ficFile_table()
#ojob.get_epubdb_ficfiles()
#ojob.update_link_db()
# ojob.reindex_fandom_by_id()
# ojob.test()
#ojob.find_reindex_targets()

#ojob.update_index_of_fandoms()
# for fic in list:
#    print(fic.FandomId)
#    print(fic.FandomUrl)
# ojob.load_fandom_info()
# ojob.create_index_of_fandoms()
print('done')

#
