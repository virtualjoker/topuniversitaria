import webapp2

from view.index import IndexHandler


app = webapp2.WSGIApplication([('/', IndexHandler)],
                              debug=True)
