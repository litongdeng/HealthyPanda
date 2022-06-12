from flask import Flask

app = Flask(__name__)
#initialize app

from teenhealth import routes
#to prevent circular imports