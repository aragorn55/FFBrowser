class Author(object):
    _AuthorID = 0
    _FFNetID = ""
    _AuthorName = ""
    _Url = ""
    def __init__(self):

        self._FFNetID = ""
        self._AuthorID = 0
        self._AuthorName = ""
        self._Url = ""

    def reset(self):
        self._FFNetID = ""
        self._AuthorID = 0
        self._AuthorName = ""
        self._Url = ""
    @property
    def AuthorID(self):
        return self._AuthorID

    @AuthorID.setter
    def AuthorID(self, vsAuthorID):
        self._AuthorID = vsAuthorID

    @property
    def FFNetID(self):
        return self._FFNetID

    @FFNetID.setter
    def FFNetID(self, vsFFNetID):
        self._FFNetID = vsFFNetID

    @property
    def AuthorName(self):
        return self._AuthorName

    @AuthorName.setter
    def AuthorName(self, vsName):
        self._AuthorName = vsName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, vsUrl):
        self._Url = vsUrl

class FanFic(object):
    _Genres = []
    _FicID = 0
    _FFNetID = ""
    _Chapters = 0
    _Fandoms = []
    _Relationships = []
    _Characters = []
    _Words = 0
    _GenreString = ""
    _Rating = ""
    _Summary = ""
    _CharactersString = ""
    _Updated = ""
    _Published = ""
    _Title = ""
    _Url = ""
    _Status = ''
    _Author = Author()

    def __init__(self):
        self._Url = ""
        self._Title = ""
        self._Published = ""
        self._Updated = ""
        self._CharactersString = ""
        self._Summary = ""
        self._Rating = ""
        self._GenreString = ""
        self._Words = 0
        self._Characters = []
        self._Relationships = []
        self._Fandoms = []
        self._Chapters = 0
        self._FFNetID = ""
        self._FicID = 0
        self._Status = ''
        self._Genres = []
        self._Author = Author()

    def reset(self):
        self._Url = ""
        self._Title = ""
        self._Published = ""
        self._Updated = ""
        self._CharactersString = ""
        self._Summary = ""
        self._Rating = ""
        self._GenreString = ""
        self._Words = 0
        self._Characters = []
        self._Relationships = []
        self._Fandoms = []
        self._Chapters = 0
        self._FFNetID = ""
        self._FicID = 0
        self._Genres = []
        self._Author.reset()
        self._Status = ''

    def setwords(self, vswords):
        swords = vswords.replace("," "")
        iwords = int(swords)
        self._Words = iwords

    @property
    def Author(self):
        return self._Author

    @Author.setter
    def Author(self, voAuthor):
        self._Author = voAuthor

    @property
    def Updated(self):
        return self._Updated

    @Updated.setter
    def Updated(self, vsUpdated):
        self._Updated = vsUpdated

    @property
    def Characters(self):
        return self._Characters

    @Characters.setter
    def Characters(self, vsCharacters):
        self._Characters = vsCharacters

    @property
    def Rating(self):
        return self._Rating

    @Rating.setter
    def Rating(self, vsRating):
        self._Rating = vsRating

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, vsTitle):
        self._Title = vsTitle

    @property
    def Url(self):
       return self._Url

    @Url.setter
    def Url(self, vsUrl):
        self._Url = vsUrl

    @property
    def FicID(self):
        return self._FicID

    @FicID.setter
    def FicID(self, ificID):
        self._FicID = ificID

    @property
    def Relationships(self):
        return self._Relationships

    @Relationships.setter
    def Relationships(self, vs_Relationships):
        self._Relationships = vs_Relationships

    @property
    def Fandoms(self):
        return self._Fandoms

    @Fandoms.setter
    def Fandoms(self, vsFandoms):
        self._Fandoms = vsFandoms

    @property
    def Words(self):
        return self._Words

    @Words.setter
    def Words(self, iWord):
        self._Words = iWord

    @property
    def Published(self):
        return self._Published

    @Published.setter
    def Published(self, vsPublished):
        self._Published = vsPublished

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, vsSummary):
        self._Summary = vsSummary

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, vStatus):
        self._Status = vStatus

    @property
    def FFNetID(self):
        return self._FFNetID

    @FFNetID.setter
    def FFNetID(self, vsFFNetID):
        self._FFNetID = vsFFNetID

    @property
    def Genres(self):
        return self._Genres

    @Genres.setter
    def Genres(self, oGenres):
        self._Genres = oGenres

    @property
    def Chapters(self):
        return self._Chapters

    @Chapters.setter
    def Chapters(self, vsChapters):
        self._Chapters = vsChapters

    @property
    def CharactersString(self):
        return self._CharactersString

    @CharactersString.setter
    def CharactersString(self, vsCharacters):
        self._CharactersString = vsCharacters