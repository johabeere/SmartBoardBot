from smartwebbot.models import Media
from smartwebbot import constants


class Document(Media):
    @classmethod
    def create(cls, user, title, data, doctype, is_upload=False, *args, **kwargs):
        document = cls(None, title)
        ##Changed back from match/case switch to dumb code due to Python 3.9.x compatability on RasPiOS til 3.10 beta release
        """match doctype:
            case "PDF": 
                document.fileType = constants.PDF 
            case "GCODE": 
                document.fileType=constants.GCODE
            case "JPEG": 
                document.fileType=constants.JPEG
            case "SVG":
                document.fileType=constants.SVG
        """
        if(doctype=="PDF"):
                document.fileType = constants.PDF
        elif(doctype=="GCODE"):
                document.fileType = constants.GCODE
        elif(doctype=="JPEG"):
                document.fileType = constants.JPEG
        elif(doctype=="SVG"):
                document.fileType = constants.SVG
        
        if (is_upload):
            document.type=constants.UPLOAD
        else:
            document.type=constants.SCAN

        document.user = user
        document.title = title
        document.data = data
        document.save()
        return document
