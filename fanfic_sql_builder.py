# joshua meyer
# Creating a new SQLite database
from CFanFic import CFanfic
import sqlite3
class FanFicSql(object):
    _Path = 'ffbrowse.db'  # name of the sqlite database file
    _get_basic_id = 'SELECT {id} from {table} WHERE {column} = ?;'

    _insert_basic = 'INSERT INTO {table}({params}) VALUES (?);'
    _insert_junction = 'INSERT INTO {table}({params}) VALUES (?,?);'
    _insert_relationship = 'INSERT INTO Relationship(FicId, RelationShipNumber, CharacterId) VALUES (?,?,?);'
    _insert_fic = 'INSERT INTO FanFic(FFNetID, Url, Title, Updated, Published, Rating, Words, Chapters, Summary) VALUES (?,?,?,?,?,?,?,?,?);'
    _select_FandomId = 'SELECT Fandom.FandomId from Fandom WHERE Fandom.FandomName = ?;'
    _select_CharacterId = 'SELECT Character.CharacterId from Character WHERE Character.CharacterName = ?;'
    _select_GenreId = 'SELECT Genre.GenreId from Genre WHERE Genre.GenreName = ?;'

    _insert_Genre = 'INSERT INTO Genre(GenreName) VALUES (?);'
    _insert_Character = 'INSERT INTO Character(CharacterName) VALUES (?);'
    _insert_Fandom = 'INSERT INTO Fandom(FandomName) VALUES (?);'
    _insert_FicGenre = 'INSERT INTO FicGenre(FicID, GenreID) VALUES (?,?);'
    _insert_FicFandom = 'INSERT INTO FicFandom(FicID, FandomID) VALUES (?,?);'
    _insert_FicCharacter = 'INSERT INTO FicCharacter(FicID, CharacterID) VALUES (?,?);'
    def __init__(self, path):
        self._Path = path

    def save_fic(self, f):
        con = sqlite3.connect(self._Path)
        cur = con.cursor()
        data = (f.FFNetID, f.Url, f.Title, f.Updated, f.Published, f.Rating, f.Words, f.Chapters, f.Summary)
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