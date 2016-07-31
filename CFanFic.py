class CFanfic(object):
    """description of class"""
    _Url = ""
    _Title = ""
    _Published = ""
    _Updated = ""
    _CharactersString = ""
    _Summary = ""
    _Rating = ""
    _GenreString = ""
    _Words = 0
    _Characters = []
    _Relationships = []
    _Fandoms = []
    _Chapters = 0
    _FFNetID = ""
    _FicID = 0
    _Genres = []

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
        self._Genres = []

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
    def FicID(self):
        return self._FicID

    @FicID.setter
    def FicID(self, ificID):
        self._FicID = ificID


    @property
    def Chapters(self):
        return self._Chapters

    @Chapters.setter
    def Chapters(self, vsChapters):
        self._Chapters = vsChapters
    @property
    def Words(self):
        return self._Words
    
    @Words.setter
    def Words(self, iWord):
        self._Words = iWord


    @property
    def Characters(self):
        return self._Characters
    
    @Characters.setter
    def Characters(self, vsCharacters):
        self._Characters = vsCharacters

    @property
    def Title(self):
        return self._Title
    
    @Title.setter
    def Title(self, vsTitle):
        self._Title = vsTitle


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
    def Url(self):
       return self._Url

    @property
    def Published(self):
        return self._Published

    @property
    def Updated(self):
        return self._Updated

    @property
    def CharactersString(self):
        return self._CharactersString
 
    @property
    def Summary(self):
        return self._Summary
    
    @Summary.setter
    def Summary(self, vsSummary):
        self._Summary = vsSummary
   
    @Url.setter
    def Url(self, vsUrl):
        self._Url = vsUrl

    @Published.setter
    def Published(self, vsPublished):
        self._Published = vsPublished

    @Updated.setter
    def Updated(self, vsUpdated):
        self._Updated = vsUpdated

    @CharactersString.setter
    def CharactersString(self, vsCharacters):
        self._CharactersString = vsCharacters

    @property
    def Rating(self):
        return self._Rating

    @Rating.setter
    def Rating(self, vsRating):
        self._Rating = vsRating

    def toFile(self):
        chars = ",".join(self._Characters)
        fan = ",".join(self._Fandoms)
        rela = ""
        for item in self._Relationships:
            rela = rela + "[" +  ",".join(item) +  "]"  

        output = self._Url + "; " + self._Title + "; " + self._Updated + "; " + self._Published + "; "+ str(self._Chapters) + "; "  + str(self._Words) + "; " + self._Summary + "; " + fan + "; " + self._Rating + "; " + chars + "; " + rela + "; " + self._GenreString
        return output

    def setwords(self, vswords):
        swords = vswords.replace("," "")
        iwords = int(swords)
        self._Words = iwords



