import attr

from app_sql import AppSql
from ffnet_fandom_info import FFNetFandomInfo
from FFNetProcess import FFNetProcess
from create_ffbrowse_db import FanFicDB


@attr.s
class FFJob(object):
    ffnet_list = []
    appdata_path = attr.ib(default='appdata.db')

    #def create_fandom_info(self, ssql, fan_url, dbPath, url, is_xover, fan_name)
    def create_fandom_info(self, ssql, fan_url, dbPath, is_xover, fan_name):
        #new_fandom = FFNetFandomInfo(0, fan_url, dbPath, url, is_xover, fan_name)
        new_fandom = FFNetFandomInfo(FandomUrl=fan_url, Fandom_DB_Path=dbPath, FandomName=fan_name)
        new_fandom.FandomName = fan_name
        new_fandom.Fandom_DB_Path = dbPath
        new_fandom.FandomUrl = fan_url
        new_fandom.Is_Xover = is_xover
        self.ffnet_list.append(new_fandom)


        ssql.save_fandom_info(new_fandom)

    def create_all_fandoms(self):
        ssql = AppSql()
        ssql._spath = 'appdata.db'
        ssql.create_settings_db()
        print("created")
        self.create_fandom_info(ssql, 'anime/Bleach/', 'bleach_ffbrowser.db', False, 'Bleach')
        print("Bleach")
        self.create_fandom_info(ssql, 'anime/Inuyasha/', 'inuyasha_ffbrowser.db', False, 'Inuyasha')
        print("Inuyasha")
        self.create_fandom_info(ssql, 'anime/Guyver/', 'guyver_ffbrowser.db', False, 'Guyver')
        print("Guyver")
        self.create_fandom_info(ssql, 'anime/Ranma/', 'ranma_ffbrowser.db', False, 'Ranma')
        print("Ranma")
        self.create_fandom_info('anime//', '_ffbrowser.db', '', False, '')
        self.create_fandom_info(ssql, 'book/Dresden-Files/', 'Dresden-Files_ffbrowser.db', False, 'Dresden Files')
        self.create_fandom_info(ssql, 'game/Devil-May-Cry/', 'Devil-May-Cry_ffbrowser.db', False, 'Devil May Cry')
        self.create_fandom_info(ssql, 'game/Halo', 'Halo_ffbrowser.db', False, 'Halo')
        self.create_fandom_info(ssql, 'Bleach-Crossovers/1758/0/', 'Bleachx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Dresden-Files-Crossovers/2489/0/', 'dresdenx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Fate-stay-night-Crossovers/2746/0/', 'fsnx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Ranma-Crossovers/93/0/', 'r12x_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Gundam-Wing-AC-Crossovers/328/0/', 'gwx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Guyver-Crossovers/473/0/', 'guyverx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Halo-Crossovers/1342/0/', 'halox_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Inuyasha-Crossovers/436/0/', 'inux_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Love-Hina-Crossovers/784/0/', 'lhx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Devil-May-Cry-Crossovers/1337/0/', 'dmcx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'F-E-A-R-Crossovers/2432/0/', 'fearx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'cartoon/Batman-Beyond/', 'bb_ffbrowser.db', False, 'Batman Beyond')
        self.create_fandom_info(ssql, 'Batman-Beyond-Crossovers/718/0/', 'bbx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'anime/Rurouni-Kenshin/', 'rk_ffbrowser.db', False, 'Rurouni Kenshin')
        self.create_fandom_info(ssql, 'Rurouni-Kenshin-Crossovers/355/0/', 'rkx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'book/Lord-of-the-Rings/', 'lotr_ffbrowser.db', False, 'Lord of the Rings')
        self.create_fandom_info(ssql, 'Lord-of-the-Rings-Crossovers/382/0/', 'lotrx_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'comic/Star-Wars/', 'sw_c_ffbrowser.db', False, 'Star Wars')
        self.create_fandom_info(ssql, 'Star-Wars-Crossovers/10797/0/', 'swx_c_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'movie/Star-Wars/', 'sw_m_ffbrowser.db', False, 'Star Wars')
        self.create_fandom_info(ssql, 'Star-Wars-Crossovers/8/0/', 'sw_c_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'tv/Dresden-Files/', 'Dresden-Files_tv_ffbrowser.db', False, 'Dresden Files')
        print('done')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')

    def load_fandom_info(self):
        ssql = AppSql()
        ssql._spath = 'appdata.db'
        fandoms = ssql.get_fandom_list()
        self.ffnet_list.extend(fandoms)

    def create_index_of_fandoms(self):
        for info in self.ffnet_list:
            self.create_index_of_fandom(info)

    def update_index_of_fandoms(self):
        for info in self.ffnet_list:
            self.update_index_of_fandom(info)

    def update_index_of_fandom(self, info):
        fictool = FFNetProcess()
        # off = FFNetProcess(path)
        # isxover = False
        # off.makeIndex("anime/Bleach/", "Bleach", isxover)

    def create_index_of_fandom(self, info):
        oDB = FanFicDB(info.Fandom_DB_Path)
        oDB.create_db(info.Fandom_DB_Path)
        off = FFNetProcess(info.Fandom_DB_Path)
        off.makeIndex(info.FandomUrl, info.FandomName, info.Is_Xover)
        # isxover = False
        # off.makeIndex("anime/Bleach/", "Bleach", isxover



