from openphoto_http import OpenPhotoHttp, OpenPhotoError, OpenPhotoDuplicateError
import api_photo
import api_tag
import api_album

class OpenPhoto(OpenPhotoHttp):
    """ Client library for OpenPhoto """
    def __init__(self, host, 
                 consumer_key='', consumer_secret='',
                 token='', token_secret=''):
        OpenPhotoHttp.__init__(self, host, 
                               consumer_key, consumer_secret,
                               token, token_secret)
 
        self.photos = api_photo.ApiPhotos(self)
        self.photo = api_photo.ApiPhoto(self)
        self.tags = api_tag.ApiTags(self)
        self.tag = api_tag.ApiTag(self)
        self.albums = api_album.ApiAlbums(self)
        self.album = api_album.ApiAlbum(self)
