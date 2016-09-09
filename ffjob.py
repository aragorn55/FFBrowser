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
        new_fandom = FFNetFandomInfo(fan_name, dbPath, fan_url)
        new_fandom.FandomName = fan_name
        new_fandom.Fandom_DB_Path = dbPath
        new_fandom.FandomUrl = fan_url
        new_fandom.Is_Xover = is_xover
        self.ffnet_list.append(new_fandom)
        ssql.save_fandom_info(new_fandom)
        return new_fandom

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
        #self.create_fandom_info('anime//', '_ffbrowser.db', '', False, '')
        self.create_fandom_info(ssql, 'book/Dresden-Files/', 'Dresden-Files_ffbrowser.db', False, 'Dresden Files')
        self.create_fandom_info(ssql, 'game/Devil-May-Cry/', 'Devil-May-Cry_ffbrowser.db', False, 'Devil May Cry')
        self.create_fandom_info(ssql, 'game/Halo/', 'Halo_ffbrowser.db', False, 'Halo')
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
        #self.create_fandom_info(ssql, '', '_ffbrowser.db', True, '')
        self.create_fandom_info(ssql, 'Overlord-Crossovers/4473/0/', 'overlord_xover_ffbrowser.db', True, '')
        print('done')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        #self.create_fandom_info('', '_ffbrowser.db', '', False, '')
        return True

    def load_fandom_info(self):
        ssql = AppSql()
        ssql._spath = 'appdata.db'
        fandoms = ssql.get_fandom_list()
        self.ffnet_list.extend(fandoms)
        return len(self.ffnet_list)


    def create_index_of_fandoms(self):
        for info in self.ffnet_list:
            self.create_index_of_fandom(info)

    def update_index_of_fandoms(self):
        for info in self.ffnet_list:
            self.update_index_of_fandom(info)

    def get_reindex_targets(self):
        reindex_list = []
        ssql = AppSql()
        ssql._spath = 'appdata.db'
        fandoms = ssql.get_fandom_list()
        for info in fandoms:
            off = FFNetProcess(info.Fandom_DB_Path)
            fandoms_fic_cnt = off.find_fandom_fic_cnt(info.FandomUrl)
            db_fic_cnt = off.get_db_fic_cnt()
            if db_fic_cnt == 0:
                reindex_list.append(info)
            elif db_fic_cnt == 25:
                reindex_list.append(info)
            elif fandoms_fic_cnt > db_fic_cnt:
                if off.is_oldest_fics_in_db(info):
                    print('db has oldest fic')
                else:
                    reindex_list.append(info)

            else:
                print('dbfic cnt = fandom fic cnt')
        print('get_reindex_targets done')
        return reindex_list

    def print_good_fandominfo(self, db_fic_cnt, fandoms_fic_cnt, info):
        target_info = 'FandomId: ' + str(info.FandomId) + ' FandomUrl: ' + str(
            info.FandomUrl) + '  good' + ' Fandom Fic cnt: ' + str(fandoms_fic_cnt) + '  db fic cnt: ' + str(db_fic_cnt)
        print(target_info)

    def print_fandom_reindex(self, db_fic_cnt, fandoms_fic_cnt, info):
        target_info = 'FandomId: ' + str(info.FandomId)
        print(target_info)
        target_info = 'FandomUrl: ' + str(info.FandomUrl)
        print(target_info)
        target_info = 'Fandom Fic cnt: ' + str(fandoms_fic_cnt)
        print(target_info)
        target_info = 'db fic cnt: ' + str(db_fic_cnt)
        print(target_info)

    def find_reindex_targets(self):
        ssql = AppSql()
        ssql._spath = 'appdata.db'
        fandoms = ssql.get_fandom_list()
        for info in fandoms:
            off = FFNetProcess(info.Fandom_DB_Path)
            fandoms_fic_cnt = off.find_fandom_fic_cnt(info.FandomUrl)
            db_fic_cnt = off.get_db_fic_cnt()
            if fandoms_fic_cnt > db_fic_cnt:
                self.print_fandom_reindex(db_fic_cnt, fandoms_fic_cnt, info)
            else:
                self.print_good_fandominfo(db_fic_cnt, fandoms_fic_cnt, info)
        print('find_reindex_targets done')
        return True







    def create_index_of_fandom(self, info):
        #self.load_fandom_info()
        oDB = FanFicDB(info.Fandom_DB_Path)
        oDB.create_db(info.Fandom_DB_Path)
        off = FFNetProcess(info.Fandom_DB_Path)
        off.index_archive(info.FandomUrl, info.FandomName, info.Is_Xover)
        # isxover = False
        # off.makeIndex("anime/Bleach/", "Bleach", isxover

    def reindex_fandom_by_id(self, Id):
        print('Reindex Fandom #' + str(Id))
        ssql = AppSql()
        ssql._spath = 'appdata.db'
        fandom = ssql.get_fandom_by_id(Id)
        off = FFNetProcess(fandom.Fandom_DB_Path)
        off.reindex_archive(fandom.FandomUrl, fandom.FandomName, fandom.Is_Xover)
        print('Reindex Fandom #' + str(Id) + ' done')
        return True

    def test(self):
        self.create_ficdb_for_fandom_by_id(30)
        self.reindex_fandom_by_id(30)
        return True
    def create_ficdb_for_fandom_by_id(self, id):
        ssql = AppSql()
        ssql._spath = 'appdata.db'
        fandom = ssql.get_fandom_by_id(id)
        ficDB = FanFicDB(fandom.Fandom_DB_Path)
        ficDB.create_db(fandom.Fandom_DB_Path)
        return True




