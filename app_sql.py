import sqlite3

import attr

from ffnet_fandom_info import FFNetFandomInfo


@attr.s
class AppSql(object):
    # _FandomInfo_create = "CREATE TABLE FFNetFandomInfo(FandomInfoId INTEGER PRIMARY KEY, FandomName TEXT, FandomUrl TEXT, Fandom_DB_Path TEXT, Url TEXT, Is_Xover BIT );"
    _FandomInfo_create = "CREATE TABLE FFNetFandomInfo(FandomInfoId INTEGER PRIMARY KEY, FandomName TEXT, FandomUrl TEXT, Fandom_DB_Path TEXT, Is_Xover BOOLEAN);"

    spath = attr.ib(default='appdata.db')
    # _insert_fandom_info = 'INSERT INTO FFNetFandomInfo(FandomName, FandomUrl, Fandom_DB_Path, Url, Is_Xover) VALUES (?,?,?,?,?);'
    _insert_fandom_info = 'INSERT INTO FFNetFandomInfo(FandomName, FandomUrl, Fandom_DB_Path, Is_Xover) VALUES (?,?,?,?);'
    _select_fandominfo_by_ID = 'SELECT * from FFNetFandomInfo WHERE FFNetFandomInfo.FandomInfoId = ?'
    _select_Id_by_Name = 'SELECT FFNetFandomInfo.FandomInfoId from FFNetFandomInfo WHERE FandomName.FandomName = ?;'
    _select_fic_by_FicID = 'SELECT * from FFNetFandomInfo WHERE FFNetFandomInfo.FandomInfoId = ?'
    _select_all_fandom_info = 'SELECT * from FFNetFandomInfo'

    def __int__(self, path):
        self._spath = path

    def create_settings_db(self):
        con = sqlite3.connect(self._spath)
        cur = con.cursor()
        cur.execute(self._FandomInfo_create)
        con.commit()
        con.close()

    def save_fandom_info(self, f):
        # f = FFNetFandomInfo()
        con = sqlite3.connect(self._spath)
        cur = con.cursor()

        data = (f.FandomName, f.FandomUrl, f.Fandom_DB_Path, f.get_is_xover_numeric())
        cur.execute(self._insert_fandom_info, data)
        con.commit()

    def get_fandom_list(self):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        select = self._select_FandomId
        fandom_list = []

        cur.execute(select)
        con.commit()
        values = cur.fetchall()
        for row in values:
            fandom = self.get_fandom_from_row(row)
            fandom_list.append(fandom)
        return fandom_list

    def get_fandom_from_row(self, row):
        ooo = FFNetFandomInfo()
        ooo.FandomId = row['FandomInfoId']
        ooo.FandomName = row['FandomName']
        ooo.FandomUrl = row['FandomUrl']
        ooo.Fandom_DB_Path = row['Fandom_DB_Path']
        # ooo.Url = row['Url']
        ooo.set_is_xover_numeric(row['Is_Xover'])
        return ooo
