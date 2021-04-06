import os 

class Config: 
   SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI") 
   FLASK_ENV=os.environ.get('FLASK_ENV')