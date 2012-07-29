import webapp2

from model.player import Player

class IndexHandler(webapp2.RequestHandler):
  """ Index view, it handlers the '/' urls call """
  def get(self):
    
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.out.write('MUDA ALGO')
