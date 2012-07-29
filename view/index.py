import webapp2
import jinja2
import os


from model.player import Player
from model.picture import Picture
from google.appengine.ext import db

jinja_environment = jinja2.Environment(
          loader=jinja2.FileSystemLoader(
            os.path.dirname(__file__)+ '/../template/'))


class IndexHandler(webapp2.RequestHandler):
  """ Index view, it handlers the '/' urls call """
  def post(self):
    self.response.out.write('METODO POST<br/>')
    opcao = self.request.get('opcao')
    self.response.out.write('Opcao:'+opcao+'<br>')
    if opcao == 'criar':
      name = self.request.get('name')
      player = Player(name=name)
      player.put()
    if opcao == 'listar':
      all_players = Player.all()
      for player in all_players:
        self.response.out.write('Player name:'+player.name+'<br>')
  
    ##################Joao Pedro#################################
    if opcao == 'upload':
      name = self.request.get('name')
      university = self.request.get('university')
      course= self.request.get('course')
      image = self.request.get('image')
      
      picture = Picture()
      
      picture.image = db.Blob(image)
      picture.name = name
      picture.name_university = university
      picture.name_course = course
      
      #self.response.out.write('name:'+name+'<br>')
      #self.response.out.write('university:'+university+'<br>')
      #self.response.out.write('course:'+course+'<br>')
      picture.put()
    ######################################################
    
    self.redirect('/')
    
    
    #####################################################
  def get(self):
    query = Player.all()
    players = query.fetch(limit=None)
    
    query = Picture.all()
    pictures = query.fetch(limit=None)
    
      
    template_values = {
        'players': players,
        'pictures': pictures,
    }
    

    
    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))
    
    #######################################################
    

    
    
    
    
