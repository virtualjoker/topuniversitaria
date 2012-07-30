import webapp2

from view.index import IndexHandler
from view.index import UploadPictureHandler
from view.index import ViewPhotoHandler


app = webapp2.WSGIApplication([('/', IndexHandler),
                               ('/upload_picture', UploadPictureHandler),
                               # nao eh nosso !!!
                               ('/view_photo/([^/]+)?', ViewPhotoHandler)
                              ],
                              debug=True)
