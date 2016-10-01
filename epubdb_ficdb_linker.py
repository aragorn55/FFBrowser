from fanfic_sql_builder import FanFicSql
import sqlite3
from fanfic import FanFic
from fanfic import Author


class DBLinker(FanFicSql):
    _insert_file_link =''
    _FicLinkCreate = "CREATE TABLE FicDbLink(FicDbLinkID INTEGER PRIMARY KEY, FicFileID INTEGER, FicId INTEGER, FanFicArchiveId TEXT, DBPath TEXT);"
    _FicCreate = "CREATE TABLE FicFile(FicId INTEGER PRIMARY KEY, FFNetID TEXT, Url TEXT, Title TEXT, AuthorId INTEGER, Updated TEXT, Published TEXT, Rating TEXT, Words INTEGER, Chapters INTEGER, Summary TEXT, Status TEXT, Packaged TEXT, FilePath TEXT);"
    _insertFicLink = 'INSERT INTO FicDbLink(FicFileID, FicId, FanFicArchiveId, DBPath) VALUES (?,?,?,?);'
    _select_ficlink_by_archive_id = 'SELECT * from FicDbLink WHERE FicDbLink.FanFicArchiveId = ?;'

    def create_file_list_db(self):
        _link_list_create = "Create TABLE FicFileList(FicFileListId INTEGER PRIMARY KEY, FicFileID INT, FanFicArchiveId TEXT, " \
                            "Url TEXT, Words INTEGER, Chapters INTEGER, Packaged TEXT, FilePath TEXT, PublisherName TEXT);"
        con = sqlite3.connect(self._FFnetArchiveLinkDB_Path)
        cur = con.cursor()
        cur.execute(_link_list_create)
        con.commit()
        con.close()
        return True

    def add_file_links_to_linkdb(self, epub_db_path):
        dbpath = self.FilePath

#        '(FicId, FFNetID, Url, Title, AuthorId, Updated, Published, Rating, Words, Chapters, Summary, Status, Packaged, FilePath)'
        select_ficfileList = 'SELECT FicFile.FicId, FicFile.FFNetID, FicFile.Url, FicFile.Words, FicFile.Chapters,' \
                           ' FicFile.Packaged, FicFile.FilePath, Publisher.PublisherName FROM FicFile, FicPublisher, ' \
                           'Publisher WHERE FicFile.FicId = FicPublisher.FicID AND FicPublisher.PublisherID = ' \
                           'Publisher.PublisherId'
        insert_filelinks  = 'INSERT INTO FicFileList(FicFileID, FanFicArchiveId, Url, Words, Chapters, ' \
                                             'Packaged, FilePath, PublisherName ) VALUES (?,?,?,?,?,?,?,?);'

        fic_list = []
        select_link_list_by_id = 'SELECT * FROM FicFile WHERE FFNetID = ? AND Fandom_DB_Path = ?'
        select_fic = self._select_fic_by_ffnet_id


        con = sqlite3.connect(epub_db_path)
        cur = con.cursor()
        linkdb_path = self._FFnetArchiveLinkDB_Path
        cur.execute(select_ficfileList)
        link_rows = cur.fetchall()
        linkdb = sqlite3.connect(linkdb_path)
        link_cur = linkdb.cursor()
        icnt = 0
        prrocessed = 0
        print('total fics in db: ' + str(len(link_rows)))
        link_cur.executemany(insert_filelinks, link_rows)
        linkdb.commit()
        linkdb.close()
        return True