"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app

# import viewertools
from FlaskWebProject1.cad.Plasma.scripts.python import viewertools

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year)


@app.route('/viewerTool', methods=['GET'])
def viewerTool():
    viewertools.show(r"D:\projects\share\data\CT\1.3.12.2.1107.5.1.4.12345.4.0.1740126031831309")


    #print("Inside Server")
    #return ("Hello World")
    ##return str(5)
    #import pdb
    #pdb.set_trace()
    #viewertools.show(r"D:\projects\share\data\CT\1.3.12.2.1107.5.1.4.12345.4.0.1740126031831309")
    #return



