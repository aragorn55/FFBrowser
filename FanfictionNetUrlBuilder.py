class FanfictionNetUrlBuilder(object):
    """description of class"""
    _http = "http://"

    _https = "https://"
    _sFFarchive = "m.fanfiction.net/"
    _protocol = ""

    _sFandomX = "Fate-stay-night-Crossovers/2746/0/"
    _sFandom = "anime/Fate-stay-night/"
    def __init__(self, fandom, protocol, sFFarchive):
        self._sFandom = fandom
        self._sFFarchive = sFFarchive
        self._protocol = protocol

    def GenerateInuyashaUrl(self, minwords, pagenum):
        sUrl = ""
        #https://m.fanfiction.net/anime/Inuyasha/?srt=1&t=0&g1=0&g2=0&r=10&lan=1&len=10&s=0&c1=650&c2=0&c3=0&c4=0&_g1=0&_c1=0&_c2=0
        sortid = self.GetSorterID()
        censorid = self.GetCensorID()
        length = self.GetLengthID(minwords)

        languageid = self.GetLanguageID()
        pageId = self.GetPageId(pagenum)

        sUrl = self._protocol + self._sFFarchive + self._sFandom
        surl = sUrl + "?" + sortid + self.Gettimerange()  + self.GetGenreID1() + self.GetGenreID2() + censorid + languageid + length
        surl = surl + self.Getstatusid() + '&c1=650&c2=0&c3=0&c4=0&_g1=0&_c1=0&_c2=0' + pageId
        return surl

    def GenerateUrl(self, minwords, pagenum):
      sUrl = ""
      sUrl = self.baseGenerateUrl( minwords, pagenum)
      return sUrl


    def baseGenerateUrl(self, minwords, pagenum):

      sUrl = ""


      sortid = self.GetSorterID()
      censorid = self.GetCensorID()
      length = self.GetLengthID(minwords)

      languageid = self.GetLanguageID()
      pageId = self.GetPageId(pagenum)

      sUrl = self._protocol + self._sFFarchive + self._sFandom
      surl = sUrl + "?" + sortid + languageid + censorid + length + pageId
      return surl



    def GetPageId(self,pagenumber):
      if pagenumber > 0:
        sval = "&p=" + str(pagenumber)
        return sval
      return ""

    def GetSorterID(self):
      sval = "&srt=" + "1"
      return sval

    def GetLengthID(self,words):
      if words == 0:
        sval = "&len=" + "0"
        return sval
      if  words == -1:

        sval = "&len=" + "11"
        return sval
      if words == -5:

        sval = "&len=" + "51"
        return sval
      if words == 1:

        sval = "&len=" + "1"
        return sval
      if words == 5:

        sval = "&len=" + "5"
        return sval
      if words == 10:

        sval = "&len=" + "10"
        return sval
      if words == 20:

        sval = "&len=" + "20"
        return sval
      if words == 40:

        sval = "&len=" + "40"
        return sval
      if words == 60:

        sval = "&len=" + "60"
        return sval
      if words == 100:

        sval = "&len=" + "100"
        return sval

      sval2 = "&len=" + "0"
      return sval2

    def GetCensorID(self):
      sval = "&r=" + "10"
      return sval

    def GetLanguageID(self):
      sval = "&lan=" + "1"
      return sval

    def GetVerseID2(self):
      s = "&v2=0"
      return s

    def GetVerseID1(self):
      s = "&v1=0"
      return s

    def Get_characterid2(self):
      s = "&_c1=0"
      return s

    def Get_characterid1(self):
      s = "&_c2=0"
      return s

    def GetCharacterID4(self):
      s = "&c4=0"
      return s

    def GetCharacterID3(self):
      s = "&c3=0"
      return s

    def GetCharacterID2(self):
      s = "&c2=0"
      return s

    def GetCharacterID1(self):
      s = "&c1=0"
      return s

    def Getstatusid(self):
      s = "&s=0"
      return s

    def Gettimerange(self):
      s = "&t=0"
      return s

    def Get_genreid1(self):
      s = "&_g1=0"
      return s

    def GetGenreID2(self):
      s = "&g1=0"
      return s

    def GetGenreID1(self):
      s = "&g2=0"
      return s


