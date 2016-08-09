from FanfictionNetUrlBuilder import FanfictionNetUrlBuilder
import time

class ExtraFFnet(object):
    _insert_basic = 'INSERT INTO {table}({params}) VALUES (?);'
    _insert_junction = 'INSERT INTO {table}({params}) VALUES (?,?);'
    _get_basic_id = 'SELECT {id} from {table} WHERE {column} = ?;'
    _get_basic_id = "SELECT {id} from {table} WHERE {column} = ?;"
    _insert_basic = "INSERT INTO {table}({params}) VALUES (?);"
    _insert_junction = "INSERT INTO {table}({params}) VALUES (?,?);"
    _insert_relationship = "INSERT INTO Relationship(FicId, RelationShipNumber, CharacterId) VALUES (?,?,?);"
    _insert_fic = "INSERT INTO FanFic(FFNetID, Url, Title, AuthorId, Updated, Published, Rating, Words, Chapters, Summary) VALUES (?,?,?,?,?,?,?,?,?);"

    def __get__Re2(self, charater_string):
        #self.story.extendList('characters', chars_ships_text.replace('[', '').replace(']', ',').split(','))
        relationship = []
        l = charater_string
        while '[' in l:
            self.story.addToList('ships', l[l.index('[') + 1:l.index(']')].replace(', ', '/'))
            l = l[l.index(']') + 1:]


    def makeInyuashaIndex(self):
        self._Fandom = "Inuyasha"
        oUrl = FanfictionNetUrlBuilder(self._Fandom, "http://", "www.fanfiction.net/")
        cnt = 3
        for x in range(cnt):
            i = x + 1
            sUrl = oUrl.GenerateInuyashaUrl(5, i)

            self.processPage(sUrl)
            print(str(i))
            time.sleep(3)