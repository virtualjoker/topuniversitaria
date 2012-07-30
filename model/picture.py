from google.appengine.ext import db
from google.appengine.ext import blobstore

class Picture(db.Model):
  """ This Model defines the picture properties"""
  
  # Image 
  image = blobstore.BlobReferenceProperty()
  
  # Person image name 
  name = db.StringProperty()
  
  # University name
  name_university = db.StringProperty()
  
  # Course name
  name_course = db.StringProperty()
