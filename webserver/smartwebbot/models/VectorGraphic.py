from smartwebbot import models, constants


class VectorGraphic(models.Media):
    @classmethod
    def create(cls, user, title, data, is_upload=False, *args, **kwargs):
        vgraphic = cls(title)
        vgraphic.fileType = constants.SVG
        if is_upload:
            vgraphic.type = constants.UPLOAD
        else:
            vgraphic.type = constants.SCAN
        vgraphic.user = user
        vgraphic.title = title
        vgraphic.data = data
        vgraphic.save()
        return vgraphic

