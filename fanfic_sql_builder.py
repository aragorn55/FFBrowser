# joshua meyer
# Creating a new SQLite database
import sqlite3

from fanfic import FanFic
from fanfic import Author


class FanFicSql(object):
    _FilePath = 'ffbrowse.db'  # name of the sqlite database file
    _insert_fic = 'INSERT INTO FanFic(FFNetID, Url, Title, AuthorId, Updated, Published, Rating, Words, ' \
                  'Chapters, Summary, Status) VALUES (?,?,?,?,?,?,?,?,?,?,?);'
    _cnt_fanfics = 'SELECT COUNT(DISTINCT FFNetID) FROM FanFic;'
    _insert_author = "INSERT INTO Author(FFNetID, AuthorName, Url) VALUES (?,?,?);"
    _select_AuthorId = 'SELECT Author.AuthorId from Author WHERE Author.FFNetID = ?;'
    _select_Author_from_id = 'SELECT * from Author WHERE Author.AuthorId = ?;'
    _insert_relationship = 'INSERT INTO Relationship(FicId, RelationShipNumber, CharacterId) VALUES (?,?,?);'
    _select_FandomId = 'SELECT Fandom.FandomId from Fandom WHERE Fandom.FandomName = ?;'
    _select_CharacterId = 'SELECT Character.CharacterId from Character WHERE Character.CharacterName = ?;'
    _select_GenreId = 'SELECT Genre.GenreId from Genre WHERE Genre.GenreName = ?;'
    _select_fic_by_ffnet_id = 'SELECT * from FanFic WHERE FanFic.FFNetID = ?;'
    _insert_Genre = 'INSERT INTO Genre(GenreName) VALUES (?);'
    _insert_Character = 'INSERT INTO Character(CharacterName) VALUES (?);'
    _insert_Fandom = 'INSERT INTO Fandom(FandomName) VALUES (?);'
    _insert_FicGenre = 'INSERT INTO FicGenre(FicID, GenreID) VALUES (?,?);'
    _insert_FicFandom = 'INSERT INTO FicFandom(FicID, FandomID) VALUES (?,?);'
    _insert_FicCharacter = 'INSERT INTO FicCharacter(FicID, CharacterID) VALUES (?,?);'
    _select_published_date = 'SELECT Fanfic.Published from Fanfic;'
    _select_newest_published = 'select Max(FanFic.Published) from FanFic;'
    _select_newest_updated = 'select Max(FanFic.Updated) from FanFic'
    _delete_FicGenre = 'DELETE FROM FicGenre WHERE FicGenre.FicID = ?;'
    _delete_FanFic = 'DELETE FROM FanFic WHERE FanFic.FicID = ?;'
    _delete_FicFandom = 'DELETE FROM FicFandom WHERE FicFandom.FicID = ?;'
    _delete_FicCharacter = 'DELETE FROM FicCharacter WHERE FicCharacter.FicID = ?;'
    _fandomcreate = "CREATE TABLE Fandom(FandomId INTEGER PRIMARY KEY , FandomName TEXT);"
    _GenreCreate = "Create TABLE Genre(GenreId INTEGER PRIMARY KEY, GenreName TEXT);"
    _FicGenresCreate = "Create TABLE FicGenre(FicGenreId INTEGER PRIMARY KEY,FicID INT, GenreID INT);"
    _FicFandomCreate = "Create TABLE FicFandom(FicFandomId INTEGER PRIMARY KEY,FicID INT, FandomId INT);"
    _CharacterCreate = "CREATE TABLE Character(CharacterId INTEGER PRIMARY KEY,CharacterName TEXT);"
    _RelationshipCreate = "CREATE TABLE Relationship(FicId INT, RelationShipNumber INT, CharacterId INT);"
    _FicCreate = "CREATE TABLE FanFic(FicId INTEGER PRIMARY KEY, FFNetID TEXT, Url TEXT, Title TEXT," \
                 " AuthorId INTEGER, Updated TEXT, Published TEXT, Rating TEXT, Words INTEGER, Chapters INTEGER, " \
                 "Summary TEXT, Status TEXT);"
    _FicCharactersCreate = "Create TABLE FicCharacter(FicCharacterId INTEGER PRIMARY KEY,FicID INT, CharacterID INT);"
    _AuthorCreate = "CREATE TABLE Author(AuthorId INTEGER PRIMARY KEY, FFNetID TEXT, AuthorName TEXT, Url TEXT);"
    _database_exists = "SELECT COUNT(*) FROM sqlite_master WHERE type = 'table' AND name = ?;"
    _select_all_fanfics = "SELECT FanFic.FFNetID, FanFic.Url, FanFic.Title, FanFic.AuthorId, FanFic.Updated, " \
                          "FanFic.Published, FanFic.Rating, FanFic.Words, FanFic.Chapters, FanFic.Summary, " \
                          "FanFic.Status From FanFic"
    _select_genres_by_ficId = 'Select Genre.GenreName from FicGenre, Genre WHERE FicGenre.GenreId = Genre.GenreId ' \
                              'AND FicGenre.FicID = ?'
    _fandom_select_by_fic = 'Select Fandom.FandomName from FicFandom, Fandom WHERE FicFandom.FandomId = ' \
                            'Fandom.FandomId AND FicFandom.FicID = ?'
    _Genre_select_by_fic = 'Select Genre.GenreName from FicGenre, Genre WHERE FicGenre.GenreId = Genre.GenreId ' \
                           'AND FicGenre.FicID = ?'
    _Character_select_by_fic = 'Select Character.CharacterName from FicCharacter, Character WHERE ' \
                               'FicCharacter.CharacterId = Character.CharacterId AND FicCharacter.FicID = ?'
    _Relationship_select_by_fic = 'Select Relationship.RelationShipNumber, Character.CharacterName from ' \
                                  'Relationship, Character WHERE Relationship.CharacterId = Character.CharacterId ' \
                                  'AND Relationship.FicID = ?'

    @property
    def FilePath(self):
        return self._FilePath

    @FilePath.setter
    def FilePath(self, vspath):
        self._FilePath = vspath

    def delete_fic(self, fic):
        fic = FanFic()
        con = sqlite3.connect(self._FilePath)
        cur = con.cursor()
        delete_fic = self._delete_FanFic
        delete_char = self._delete_FicCharacter
        delete_fan = self._delete_FicFandom
        delete_genre = self._delete_FicGenre
        cur.execute(delete_fic, (fic.FicID,))
        cur.execute(delete_char, (fic.FicID,))
        cur.execute(delete_fan, (fic.FicID,))
        cur.execute(delete_genre, (fic.FicID,))
        con.commit()

    def get_fanfic_cnt(self):
        con = sqlite3.connect(self._FilePath)
        cur = con.cursor()
        cur.execute(self._cnt_fanfics)
        fic_cnt = cur.fetchall()[0][0]
        return fic_cnt

    def get_newest_date(self):
        dbpath = self.FilePath
        con = sqlite3.connect(dbpath)
        cur = con.cursor()
        cur.execute(self._select_newest_published)
        new_pubs = cur.fetchall()
        cur.execute(self._select_newest_updated)
        new_ups = cur.fetchall()
        ipub = self.convert_rows_to_int(new_pubs)
        iup = self.convert_rows_to_int(new_ups)
        if ipub > iup:
            return ipub
        else:
            return iup

    def convert_rows_to_int(self, row_list):
        row = row_list[0]
        col = row[0]
        if col is None:
            return 0

        elif col.isnumeric():
            return int(col)
        else:
            return 0

    def get_fic_by_ffnetID(self, ffnetid):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        select_fic = self._select_fic_by_ffnet_id
        cur.execute(select_fic, (ffnetid,))
        fic_rows = cur.fetchall()
        fic_row = fic_rows[0]
        fic = self.convert_row_to_fic(fic_row)
        fic.Author = self.get_author_by_id(fic_row[4])
        return fic

    def is_fic_in_Db(self, ffnetid):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        fic_list = []
        select_fic = self._select_fic_by_ffnet_id

        cur.execute(select_fic, (ffnetid,))
        rows = cur.fetchall()
        if len(rows) == 0:
            return False
        else:
            return True

    def get_author_by_id(self, vId):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        fic_list = []
        select_a = self._select_Author_from_id
        cur.execute(select_a, (vId,))
        a_rows = cur.fetchall()
        oAuthor = Author()
        if len(a_rows) > 0:
            a_row = a_rows[0]
            oAuthor.AuthorID = a_row[0]
            oAuthor.FFNetID = a_row[1]
            oAuthor.AuthorName = a_row[2]
            oAuthor.Url = a_row[3]
        return oAuthor

    def get_all_fanfics(self, IsXover):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        fanfic_list = []
        select_fic = self._select_all_fanfics
        cur.execute(select_fic)
        fic_rows = cur.fetchall()
        print(str(len(fic_rows)))
        for row in fic_rows:
            fic = self.convert_row_to_fic(row)
            fic.Is_Xover = IsXover
            fic.Author = self.get_author_by_id(fic.Author.AuthorID)
            cur.execute(self._fandom_select_by_fic, (fic.FicID,))
            fan_rows = cur.fetchall()
            for fan_row in fan_rows:
                fic.Fandom.append(fan_row[0])
            cur.execute(self._Genre_select_by_fic, (fic.FicID,))
            fan_rows = cur.fetchall()
            for fan_row in fan_rows:
                fic.Genres.append(fan_row[0])
            cur.execute(self._Character_select_by_fic, (fic.FicID,))
            char_rows = cur.fetchall()
            for char_row in char_rows:
                fic.Characters.append(char_row[0])
            cur.execute(self._Relationship_select_by_fic, (fic.FicID,))
            rel_rows = cur.fetchall()
            rel_num = 0
            relationship = []
            if len(rel_rows) > 0:
                rel_num = rel_rows[0][0]
            for rel_row in rel_rows:
                if rel_row[0] != rel_num:
                    fic.Relationships.append(relationship)
                    relationship = []
                    rel_num = rel_row[0]
                relationship.append(rel_row[1])
            if len(relationship) > 0:
                fic.Relationships.append(relationship)
            fanfic_list.append(fic)
            print('fic loaded')
        return fanfic_list



    def save_fic(self, fic):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        fic_list = []
        select_fic = self._select_fic_by_ffnet_id

        cur.execute(select_fic, (fic.FFNetID,))
        rows = cur.fetchall()
        if len(rows) == 0:
            self.insert_fic(fic)
        else:
            item = rows[0]
            oldfic = self.convert_row_to_fic(item)
            if fic.get_date_comparison() > oldfic.get_date_comparison():
                self.delete_fic(oldfic)
                self.insert_fic(fic)

                # fic_list.append(fic)
                # ofic  = fic_list[0]

    def convert_row_to_fic(self, item):
        fic = FanFic()
        fic.FicId = item[0]
        fic.FFNetID = item[1]
        fic.Url = item[2]
        fic.Title = item[3]
        fic.Author.AuthorID = item[4]
        fic.Updated = str(item[4])
        fic.Published = str(item[5])
        fic.Rating = item[6]
        fic.Words = item[7]
        fic.Chapters = item[8]
        fic.Summary = item[9]
        fic.Status = item[10]
        return fic

    def __init__(self, path):
        self._FilePath = path

    def save_author(self, voAuthor):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()

        select = self._select_AuthorId
        item = voAuthor.FFNetID
        o = (item,)
        cur.execute(select, o)
        con.commit()
        value = cur.fetchall()
        rowid = 0
        if len(value) == 0:
            insert = self._insert_author
            data = (voAuthor.FFNetID, voAuthor.AuthorName, voAuthor.Url)
            cur.execute(self._insert_author, data)
            # cur.execute(insert, o)
            con.commit()
            rowid = cur.lastrowid
            return rowid
        else:
            row = value[0]
            rowid = row[0]
            rowid = int(rowid)
            return rowid
        return rowid

    def insert_fic(self, f):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()

        f.Author.AuthorID = self.save_author(f.Author)
        data = (
            f.FFNetID, f.Url, f.Title, f.Author.AuthorID, f.Updated, f.Published, f.Rating, f.Words, f.Chapters,
            f.Summary,
            f.Status)
        cur.execute(self._insert_fic, data)
        con.commit()
        ficid = cur.lastrowid
        if len(f.Genres) > 0:
            self.save_FicGenre(f.Genres, ficid)
        self.save_FicFandom(f.Fandoms, ficid)
        if len(f.Characters) > 0:
            self.save_FicCharacter(f.Characters, ficid)

        if len(f.Relationships) > 0:
            self.save_relationships(f.Relationships, ficid)
        return ficid

    def save_FicGenre(self, genres, ficId):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        genre_ids = self.save_Genres(genres)
        for x in range(len(genre_ids)):
            genre_id = genre_ids[x]
            genre_id = int(genre_id)
            genretupal = (ficId, genre_id)
            insert = self._insert_FicGenre
            # cur.execute(self._insert_FicGenre, genretupal)
            cur.execute(self._insert_FicGenre, genretupal)
            con.commit()

    def save_FicCharacter(self, characters, ficId):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        CharacterIds = self.save_Characters(characters)
        for x in range(len(CharacterIds)):
            CharacterId = CharacterIds[x]
            characterTupal = (CharacterId, ficId)
            insert = self._insert_FicGenre
            # cur.execute(self._insert_FicCharacter, characterTupal)
            cur.execute(self._insert_FicCharacter, (ficId, int(CharacterId)))
            con.commit()

    def save_FicFandom(self, fandoms, ficId):
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        fandom_ids = self.save_Fandoms(fandoms)
        for x in range(len(fandom_ids)):
            fandom_id = fandom_ids[x]
            Fandomtupal = (ficId, fandom_id)
            insert = self._insert_FicFandom
            # cur.execute(self._insert_FicFandom, Fandomtupal)
            cur.execute(self._insert_FicFandom, (ficId, int(fandom_id)))
            con.commit()

    def save_Genres(self, voList):
        GenreId_list = []
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        for x in range(len(voList)):
            select = self._select_GenreId
            item = voList[x]
            o = (item,)
            cur.execute(select, o)
            con.commit()
            value = cur.fetchall()
            rowid = 0
            if len(value) == 0:
                insert = self._insert_Genre
                cur.execute(insert, o)
                con.commit()
                rowid = cur.lastrowid
                GenreId_list.append(rowid)
            else:
                row = value[0]
                rowid = row[0]
                rowid = int(rowid)
                GenreId_list.append(rowid)
        return GenreId_list

    def save_Fandoms(self, voList):
        FandomId_list = []
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        for x in range(len(voList)):
            select = self._select_FandomId
            item = voList[x]
            o = (item,)
            cur.execute(select, o)
            con.commit()
            value = cur.fetchall()
            rowid = 0
            if len(value) == 0:
                insert = self._insert_Fandom
                cur.execute(insert, o)
                con.commit()
                rowid = cur.lastrowid
                FandomId_list.append(rowid)
            else:
                row = value[0]
                rowid = row[0]
                rowid = int(rowid)
                FandomId_list.append(rowid)

        return FandomId_list

    def save_Characters(self, voList):
        CharacterId_list = []
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        for x in range(len(voList)):
            select = self._select_CharacterId
            item = voList[x]
            o = (item,)
            cur.execute(select, o)
            con.commit()
            value = cur.fetchall()
            rowid = 0
            if len(value) == 0:
                insert = self._insert_Character
                cur.execute(insert, o)
                con.commit()
                rowid = cur.lastrowid
                CharacterId_list.append(rowid)
            else:
                row = value[0]
                rowid = row[0]
                rowid = int(rowid)
                CharacterId_list.append(rowid)

        return CharacterId_list

    def save_relationships(self, voList, ficid):
        charId_list = []
        result = []
        dbpath = self.FilePath 

        con = sqlite3.connect(dbpath)

        cur = con.cursor()
        for i in range(len(voList)):
            charIds = self.save_Characters(voList[i])

            for x in range(len(charIds)):
                charId = charIds[x]
                data = (ficid, i, charId)
                cur.execute(self._insert_relationship, data)
                con.commit()

        return charId_list

    def set_path(self, path):
        self._FilePath = path

    def create_db(self, path):
        con = sqlite3.connect(path)
        cur = con.cursor()
        is_set = self.is_db_set_up(cur)

        if not is_set:
            cur.execute(self._fandomcreate)
            cur.execute(self._AuthorCreate)
            cur.execute(self._GenreCreate)
            cur.execute(self._CharacterCreate)
            cur.execute(self._FicCreate)
            cur.execute(self._FicGenresCreate)
            cur.execute(self._FicFandomCreate)
            cur.execute(self._RelationshipCreate)
            cur.execute(self._FicCharactersCreate)

        # cur.execute(self._database_exists, ('',))
        # cur.execute(self._database_exists, ('',))
        # cur.execute(self._database_exists, ('',))
        # cur.execute(self._database_exists, ('',))

        con.commit()
        con.close()

    def test_table(self, cur, table):
        cur.execute(self._database_exists, (table,))
        a_row = cur.fetchone()
        if int(a_row[0]) == 0:
            return False
        else:
            return True

    def is_db_set_up(self, cur):
        if not self.test_table(cur, 'Fandom'):
            return False

        if not self.test_table(cur, 'Genre'):
            return False

        if not self.test_table(cur, 'FicGenre'):
            return False
        if not self.test_table(cur, 'FicFandom'):
            return False
        if not self.test_table(cur, 'Character'):
            return False
        if not self.test_table(cur, 'Relationship'):
            return False
        if not self.test_table(cur, 'FanFic'):
            return False
        if not self.test_table(cur, 'FicCharacter'):
            return False
        if not self.test_table(cur, 'Author'):
            return False
        return True
