# joshua meyer
# Creating a new SQLite database
import sqlite3


from fanfic import FanFic
from fanfic import Author



class FanFicSql(object):
    _Path = 'ffbrowse.db'  # name of the sqlite database file
    _insert_fic = 'INSERT INTO FanFic(FFNetID, Url, Title, AuthorId, Updated, Published, Rating, Words, Chapters, Summary, Status) VALUES (?,?,?,?,?,?,?,?,?,?,?);'
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

    def delete_fic(self, fic):
        fic = FanFic()
        con = sqlite3.connect(self._Path)
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
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        cur.execute(self._cnt_fanfics)
        fic_cnt = cur.fetchall()[0][0]
        return fic_cnt

    def get_newest_date(self):
        con = sqlite3.connect(self._Path)
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
        if col == None:
            return 0

        elif col.isnumeric():
            return int(col)
        else:
            return 0

    def get_fic_by_ffnetID(self, ffnetid):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        select_fic = self._select_fic_by_ffnet_id
        cur.execute(select_fic, (ffnetid,))
        fic_rows = cur.fetchall()
        fic_row = fic_rows[0]
        fic = self.convert_row_to_fic(fic_row)
        fic.Author = self.get_author_by_id(fic_row[4])
        return fic

    def is_fic_in_Db(self, ffnetid):
        con = sqlite3.connect(self._Path)
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
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        fic_list = []
        select_a = self._select_Author_from_id
        cur.execute(select_a, (vId,))
        a_row = cur.fetchone()
        oAuthor = Author()
        oAuthor.AuthorID = a_row[0]
        oAuthor.FFNetID = a_row[1]
        oAuthor.AuthorName = a_row[2]
        oAuthor.Url = a_row[3]
        return oAuthor




    def save_fic(self, fic):
        con = sqlite3.connect(self._Path)
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

        #fic_list.append(fic)
        #ofic  = fic_list[0]

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
        self._Path = path

    def save_author(self, voAuthor):
        con = sqlite3.connect(self._Path)
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
            #cur.execute(insert, o)
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
        con = sqlite3.connect(self._Path)
        cur = con.cursor()

        f.Author.AuthorID = self.save_author(f.Author)
        data = (f.FFNetID, f.Url, f.Title, f.Author.AuthorID, f.Updated, f.Published, f.Rating, f.Words, f.Chapters, f.Summary, f.Status)
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
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        genre_ids = self.save_Genres(genres)
        for x in range(len(genre_ids)):
            genre_id = genre_ids[x]
            genre_id = int(genre_id)
            genretupal = (ficId, genre_id)
            insert = self._insert_FicGenre
            #cur.execute(self._insert_FicGenre, genretupal)
            cur.execute(self._insert_FicGenre, genretupal)
            con.commit()

    def save_FicCharacter(self, characters, ficId):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        CharacterIds = self.save_Characters(characters)
        for x in range(len(CharacterIds)):
            CharacterId = CharacterIds[x]
            characterTupal = (CharacterId, ficId)
            insert = self._insert_FicGenre
            #cur.execute(self._insert_FicCharacter, characterTupal)
            cur.execute(self._insert_FicCharacter, (ficId, int(CharacterId)))
            con.commit()

    def save_FicFandom(self, fandoms, ficId):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        fandom_ids = self.save_Fandoms(fandoms)
        for x in range(len(fandom_ids)):
            fandom_id = fandom_ids[x]
            Fandomtupal = (ficId, fandom_id)
            insert = self._insert_FicFandom
            #cur.execute(self._insert_FicFandom, Fandomtupal)
            cur.execute(self._insert_FicFandom, (ficId, int(fandom_id)))
            con.commit()

    def save_Genres(self, voList):
        GenreId_list = []
        con = sqlite3.connect(self._Path)
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
        con = sqlite3.connect(self._Path)
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
        con = sqlite3.connect(self._Path)
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
        con = sqlite3.connect(self._Path)
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
        self._Path = path


