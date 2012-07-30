from google.appengine.ext import db
from google.appengine.ext import blobstore


class Player(db.Model):
  """ This Model defines players properties."""
  
  # Googles user
  user = db.UserProperty()
  
  # Players name
  name = db.StringProperty()
  
  # Players picture
  picture = blobstore.BlobReferenceProperty()
  
  # Pair is missing
  # pair = reference property
