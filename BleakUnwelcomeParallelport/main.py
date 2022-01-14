from datetime import datetime
from application.models import db
from application.api import *
from flask import Flask,request,render_template,session,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
app=Flask(__name__)
app.secret_key="qsdcergth!@#$%^&*("  
a={'!','@','#','$','%','/','^','&','*','>','<','{','}',']','[',"'",'"',",",'-',"|",'~',"`"}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
api.add_resource(hell2,'/api/deck','/api/deck/<deck_name>','/api/deck/<deck_name>/<user_id>')
api.add_resource(hell, '/api/card/<card_id>','/api/card')
api.add_resource(hell3, '/api/score/<user_id>')
db=SQLAlchemy(app)
app.app_context().push()
from application.controllers import *
if __name__=="__main__":
    app.run(host = "0.0.0.0", debug=True)