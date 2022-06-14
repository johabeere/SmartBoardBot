from smartwebbot.models import Media
from smartwebbot import constants


class Image(Media):
    @classmethod
    def create(cls, user, title, data, filetype, is_upload=False, *args, **kwargs):
        image = cls(title)
        image.fileType = filetype
        if is_upload:
            image.type = constants.UPLOAD
        else:
            image.type = constants.SCAN
        image.user = user
        image.title = title
        image.data = data
        image.save()
        return image
    