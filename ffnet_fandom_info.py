import attr


@attr.s
class FFNetFandomInfo(object):
    FandomName = attr.ib()
    Fandom_DB_Path = attr.ib()
    FandomUrl = attr.ib()

#    Url = attr.ib()

    FandomId = attr.ib(default=0)
    Is_Xover = attr.ib(default=False)
    def get_is_xover_numeric(self):
        if self.Is_Xover:
            return 1
        else:
            return 0
    def __init__(self):
        self.Is_Xover = False
        self.FandomUrl = ''
        self.Fandom_DB_Path = ''
        self.FandomName = ''
        self.FandomId = 0
    def set_is_xover_numeric(self, isxover):
        if isxover == 1:
            self.Is_Xover = True
        elif isxover == 0:
            self.Is_Xover = False