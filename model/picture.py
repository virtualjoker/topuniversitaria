from google.appengine.ext import db


class Picture(db.Model):
  """ This Model defines the picture properties"""
  
  # Image 
  image = db.BlobProperty()
  
  # Person image name 
  name = db.StringProperty()
  
  # University name
  name_university = db.StringProperty()
  
  # Course name
  name_course = db.StringProperty()
