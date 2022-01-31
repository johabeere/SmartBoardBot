from smartwebbot.models import Media
from smartwebbot import constants


class Document(Media):
    @classmethod
    def create(cls, user, title, data, is_upload=True, *args, **kwargs):
        document = cls(None, title)
        document.fileType = constants.PDF
        if is_upload:
            document.type = constants.UPLOAD
        else:
            document.type = constants.SCAN
        document.user = user
        document.title = title
        document.data = data
        document.save()
        return document
