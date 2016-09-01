# joshua meyer
# Creating a new SQLite database
from CFanFic import CFanfic
import sqlite3
class FanFicDB(object):
    _Path = 'ffbrowse.db'  # name of the sqlite database file
    _fandomcreate = "CREATE TABLE Fandom(FandomId INTEGER PRIMARY KEY , FandomName TEXT);"
    _GenreCreate = "Create TABLE Genre(GenreId INTEGER PRIMARY KEY, GenreName TEXT);"
    _FicGenresCreate = "Create TABLE FicGenre(FicGenreId INTEGER PRIMARY KEY,FicID INT, GenreID INT);"
    _FicFandomCreate = "Create TABLE FicFandom(FicFandomId INTEGER PRIMARY KEY,FicID INT, FandomId INT);"
    _CharacterCreate = "CREATE TABLE Character(CharacterId INTEGER PRIMARY KEY,CharacterName TEXT);"
    _RelationshipCreate = "CREATE TABLE Relationship(FicId INT, RelationShipNumber INT, CharacterId INT);"
    _FicCreate = "CREATE TABLE FanFic(FicId INTEGER PRIMARY KEY, FFNetID TEXT, Url TEXT, Title TEXT, AuthorId INTEGER, Updated TEXT, Published TEXT, Rating TEXT, Words INTEGER, Chapters INTEGER, Summary TEXT, Status TEXT);"
    _FicCharactersCreate = "Create TABLE FicCharacter(FicCharacterId INTEGER PRIMARY KEY,FicID INT, CharacterID INT);"
    _AuthorCreate = "CREATE TABLE Author(AuthorId INTEGER PRIMARY KEY, FFNetID TEXT, AuthorName TEXT, Url TEXT);"
    def __init__(self, path):
        self._Path = path



    def create_db(self, path):
        con = sqlite3.connect(path)
        cur = con.cursor()
        cur.execute(self._fandomcreate)
        cur.execute(self._AuthorCreate)
        cur.execute(self._GenreCreate)
        cur.execute(self._CharacterCreate)
        cur.execute(self._FicCreate)
        cur.execute(self._FicGenresCreate)
        cur.execute(self._FicFandomCreate)
        cur.execute(self._RelationshipCreate)
        cur.execute(self._FicCharactersCreate)

        con.commit()
        con.close()


    def set_path(self, path):
        self._Path = path



