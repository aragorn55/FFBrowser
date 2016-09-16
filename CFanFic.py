from fanfic import FanFic
from fanfic_sql_builder import FanFicSql


class CFanfic(FanFic):
    """description of class"""

    def toFile(self, ofic):
        chars = ",".join(ofic.Characters)
        fan = ",".join(ofic.Fandoms)
        rela = ""
        for item in ofic.Relationships:
            rela = rela + "[" + ",".join(item) + "]"

        output = ofic.Url + "; " + ofic.Title + "; " + ofic.Updated + "; " + ofic.Published + "; " \
                 + str(ofic.Chapters) + "; " + str(ofic.Words) + "; " + ofic.Summary + "; " + fan + "; " \
                 + ofic.Rating + "; " + chars + "; " + rela + "; " + ofic.GenreString
        return output

    def insert_to_db(self, path):
        oDB = FanFicSql(path)
