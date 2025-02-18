from flask import Blueprint

# Define a Blueprint for this module (mchat)
# irsystem = Blueprint('irsystem',
#                      __name__,
#                      url_prefix='/',
#                      static_folder='../static',
#                      template_folder='../templates')
irsystem = Blueprint('irsystem',
                     __name__,
                     static_folder='../frontend/build/static',
                     template_folder='../frontend/build',
                     url_prefix='/api')
# Import all controllers
from .controllers.search_controller import *