import webapp2

from model.player import Player

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
  
  
  def get(self):
    
    self.response.headers['Content-Type'] = 'text/html'
    self.response.out.write('MUDA ALGO')
    self.response.out.write('<form method="POST">')
    self.response.out.write('<input type="text" name="name" />')
    self.response.out.write('<input type="submit" name="opcao" value="criar" />')
    self.response.out.write('<input type="submit" name="opcao" value="listar" />')
    self.response.out.write('</form>')
