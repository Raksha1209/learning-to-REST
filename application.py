from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///snacks.db'
db = SQLAlchemy(app)

class Snack(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    description= db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.name}-{self.description}"

class Drink(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(80),unique=True,nullable=False)
    description= db.Column(db.String(120))
    
    def __repr__(self):
        return f"{self.name}-{self.description}"


@app.route('/')
def index():
    return "Hello, World!"

# GET REQUESTS 
@app.route('/drinks')
def get_drinks():
    
    drinks = [
        {"id": 1, "name": "Coke"},
        {"id": 2, "name": "Pepsi"},
        {"id": 3, "name": "Sprite"}
    ]
    return {"drinks": drinks}  

@app.route('/snacks')
def get_snacks(): 
    snacks=Snack.query.all()
    output=[]
    for snack in snacks:
        snack_data = { 'name' :snack.name, 'description':snack.description}
        output.append(snack_data)
    return {"snacks": output}