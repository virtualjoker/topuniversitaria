import webapp2
import jinja2
import os


from model.player import Player
from model.picture import Picture
from google.appengine.ext import db

from google.appengine.api import users
from google.appengine.ext import blobstore
from google.appengine.ext.webapp import blobstore_handlers


jinja_environment = jinja2.Environment(
          loader=jinja2.FileSystemLoader(
            os.path.dirname(__file__)+ '/../template/'))



class ViewPhotoHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, photo_key):
        if not blobstore.get(photo_key):
            self.error(404)
        else:
            self.send_blob(photo_key)


class UploadPictureHandler(blobstore_handlers.BlobstoreUploadHandler):
  ''' Essa classe vai receber o formulario que tem a foto da guria '''
  def post(self):
    try:
      name = self.request.get('name')
      university = self.request.get('university')
      course= self.request.get('course')
      
      upload = self.get_uploads()[0]
      
      picture = Picture()
      picture.image = upload.key()
      picture.name = name
      picture.name_university = university
      picture.name_course = course
      
      db.put(picture)

      self.redirect('/view_photo/%s' % upload.key())
      #self.response.out.write('TUDO FUNCIONOU OK!!!!')

    except:
      #self.redirect('/upload_failure.html')
      self.response.out.write('FALHOUUUUU FUDEUUUU!')




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
      
      """picture.image = db.Blob(image)
      picture.name = name
      picture.name_university = university
      picture.name_course = course"""
      
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
    
    
    upload_picture = blobstore.create_upload_url('/upload_picture')
    
      
    template_values = {
        'players': players,
        'pictures': pictures,
        'upload_picture': upload_picture,
    }
    

    
    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))
    
    #######################################################
    
    ######################################################
    
    
   
            
    
    
    ######################################################
    
    
    
    
