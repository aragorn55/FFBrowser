class FFNetFandomInfo(object):
    _Is_Xover = False
    #    Url = attr.ib()
    _FandomName = ''
    _Fandom_DB_Path = ''
    _FandomUrl = ''
    _FandomId = -1

    @property
    def FandomName(self):
        return self._FandomName

    @FandomName.setter
    def FandomName(self, voFandomName):
        self._FandomName = voFandomName

    @property
    def Fandom_DB_Path(self):
        return self._Fandom_DB_Path

    @Fandom_DB_Path.setter
    def Fandom_DB_Path(self, voFandom_DB_Path):
        self._Fandom_DB_Path = voFandom_DB_Path

    @property
    def FandomUrl(self):
        return self._FandomUrl

    @FandomUrl.setter
    def FandomUrl(self, voFandomUrl):
        self._FandomUrl = voFandomUrl

    @property
    def FandomId(self):
        return self._FandomId

    @FandomId.setter
    def FandomId(self, voFandomId):
        self._FandomId = voFandomId

    @property
    def Is_Xover(self):
        return self._Is_Xover

    @Is_Xover.setter
    def Is_Xover(self, voIs_Xover):
        self._Is_Xover = voIs_Xover

    def get_is_xover_numeric(self):
        if self.Is_Xover:
            return 1
        else:
            return 0

    def __init__(self):
        self._Is_Xover = False
        self._FandomUrl = ''
        self._Fandom_DB_Path = ''
        self._FandomName = ''
        self._FandomId = 0

    def set_is_xover_numeric(self, isxover):
        if isxover == 1:
            self._Is_Xover = True
        elif isxover == 0:
            self._Is_Xover = False
