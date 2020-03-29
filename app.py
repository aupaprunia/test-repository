from flask import Flask,request
from flask_restful import Resource, Api
from flask_jwt import JWT,jwt_required

from security import authenticate,identity
from resources.user import UserRegister
from resources.patient import Patient,all_Patients
from resources.hospital import Hospital, all_Hospitals
from db import db

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
api=Api(app)
app.secret_key="aditya"

@app.before_first_request
def create_tables():
    db.create_all()

jwt=JWT(app,authenticate,identity)

api.add_resource(Patient,'/patient/<string:name>')
api.add_resource(all_Patients,'/allPatients')

api.add_resource(Hospital,'/hospital/<string:name>')
api.add_resource(all_Hospitals,'/allHospitals')

api.add_resource(UserRegister,'/register')

if __name__=='__main__':
    db.init_app(app)
    app.run(debug=True,port=8000)