from google.appengine.ext import db


class Player(db.Model):
  """ This Model defines players properties."""
  
  # Googles user
  user = db.UserProperty()
  
  # Players name
  name = db.StringProperty()
  
  # Players picture
  picture = db.BlobProperty()
  
  # Pair is missing
  # pair = reference property
