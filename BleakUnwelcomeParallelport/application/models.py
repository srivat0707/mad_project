from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy()
class users(db.Model):
    id=db.Column("id",db.Integer,primary_key=True,autoincrement=True)
    name=db.Column("name",db.String,nullable=False)
    password=db.Column("password",db.String,nullable=False,unique=True)
    def __init__(self,name,password):
        self.name=name
        self.password=password
class decks(db.Model):
    deck_id=db.Column("deck_id",db.Integer,primary_key=True,autoincrement=True)
    deck_name=db.Column("deck_name",db.String,nullable=False,unique=True)
    def __init__(self,name):
        self.deck_name=name
class scores(db.Model):
    deck_id=db.Column("deck_id",db.Integer,db.ForeignKey("decks.deck_id"),primary_key=True)
    id=db.Column("id",db.Integer,db.ForeignKey("users.id"),primary_key=True)
    score=db.Column("score",db.Integer)
    time=db.Column("time",db.String)
    def __init__(self,deck_id,id,score,time):
        self.deck_id=deck_id
        self.id=id
        self.score=score
        self.time=time
class cards(db.Model):
    deck_id=db.Column("deck_id",db.Integer,db.ForeignKey("decks.deck_id"),primary_key=True,nullable=False)
    card_id=db.Column("card_id",db.Integer,primary_key=True,autoincrement=True)
    front=db.Column("front",db.String,nullable=False)
    back=db.Column("back",db.String,nullable=False)
    def __init__(self,deck_id,front,back):
        self.deck_id=deck_id
        self.front=front
        self.back=back