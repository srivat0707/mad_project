from flask_restful import Resource, Api, reqparse
from application.models import *
#hell for cards
#hell2 for decks
#hell3 for score 
class hell2(Resource):
    def get(self,deck_name):
        try:
            s=decks.query.filter_by(deck_name=deck_name).first()
            if s is None:
                return "deck not found",404
            res=[]
            q=cards.query.filter_by(deck_id=s.deck_id).all()
            for i in q:
                res.append(i.card_id)
            return ({"deck_id": s.deck_id,"deck_name": s.deck_name,"cards":res},200 )
        except:
            return "Internal Server Error",500
    def put(self,deck_name):
        try:
            put_args = reqparse.RequestParser()
            put_args.add_argument("deck_name")
            args = put_args.parse_args()
            new_deck_name = args.get('deck_name',None)
            s=decks.query.filter_by(deck_name=deck_name).first()
            if s is None:
                return "deck not found",404
            if deck_name==None or type(deck_name)!=str:
                return {"error_code":"DECK001","error_message":"Deck Name is required and should be string"},400
        
            s.deck_name=new_deck_name
            db.session.commit()
            return ({"deck_id": s.deck_id,"deck_name": s.deck_name},200)
        except:
            return "Internal Server Error",500 

    def post(self):
        put_args = reqparse.RequestParser()
        put_args.add_argument("deck_name")
        args = put_args.parse_args()
        dec_name = args.get('deck_name',None)
        s=decks.query.filter_by(deck_name=dec_name).first()
        if s is not None:
            return "decks already exist",409
        if dec_name==None or type(dec_name)!=str:
            return {"error_code":"DECK001","error_message":"Deck Name is required and should be string"},400
    
        s_new=decks(dec_name)
        db.session.add(s_new)
        db.session.commit()
        return ({"deck_id": s_new.deck_id,"deck_name": s_new.deck_name},201 )

    def delete(self,deck_name,user_id):
        try:
          check=users.query.filter_by(id=user_id).first()
          if check is None:
            return "user not found",404
          s=decks.query.filter_by(deck_name=deck_name).first()
          if s is None:
            return "deck not found",404
          q=cards.query.filter_by(deck_id=s.deck_id).all()
          e=scores.query.filter_by(deck_id=s.deck_id,id=user_id).first()
          for i in q:
            db.session.delete(i)
          db.session.delete(s)
          if e:
            db.session.delete(e)
          db.session.commit()
          return 	"Successfully Deleted",200 
        except:
          return "Internal Server Error",500
  
class hell(Resource):
    def get(self,card_id):
        try:
            s=cards.query.filter_by(card_id=card_id).first()
            if s is None:
                return "card not found",404
            return ({"front": s.front,"back": s.back},200 )
        except:
            return "Internal Server Error",500
    def put(self,card_id):
        try:
            put_args = reqparse.RequestParser()
            put_args.add_argument("front")
            put_args.add_argument("back")
            args = put_args.parse_args()
            c_front = args.get('front',None)
            c_back=args.get("back",None)
            
            s=cards.query.filter_by(card_id=card_id).first()
            if s is None:
                return "Card not found",404
            if c_front==None or type(c_front)!=str:
                return {"error_code":"CARD001","error_message":"FRONT is required and should be string"},400
            if c_back==None or type(c_back)!=str:
                return {"error_code":"CARD002","error_message":"BACK is required and should be string"},400 
        
            s.front=c_front
            s.back=c_back
            db.session.commit()
            return ({"front": s.front,"back": s.back},200)
        except:
            return "Internal Server Error",500
    def delete(self,card_id):
        try:
          s=cards.query.filter_by(card_id=card_id).first()
          if s is None:
            return "card not found",404
          db.session.delete(s)
          db.session.commit()
          return 	"Successfully Deleted",200 
        except:
          return "Internal Server Error",500
    def post(self):
        put_args = reqparse.RequestParser()
        put_args.add_argument("deck_name")
        put_args.add_argument("front")
        put_args.add_argument("back")
        args = put_args.parse_args()
        dec_name = args.get('deck_name',None)
        c_front=args.get("front",None)
        c_back= args.get("back",None)
        s=decks.query.filter_by(deck_name=dec_name).first()
        print(s)
        if s is  None:
            return "decks doesnot exist",409
        if dec_name==None or type(dec_name)!=str:
            return {"error_code":"DECK001","error_message":"Deck Name is required and should be string"},400
        if c_front==None or type(c_front)!=str:
            return {"error_code":"CARD001","error_message":"FRONT is required and should be string"},400
        if c_back!=None and type(c_back)!=str:
            return {"error_code":"CARD002","error_message":"BACK is required and should be string"},400 
        s_new=cards(s.deck_id,c_front,c_back)
        db.session.add(s_new)
        db.session.commit()
        return ({"deck_id":s_new.deck_id,"front": s_new.front,"back": s_new.back},201 ) 

class hell3(Resource):
    def get(self,user_id):
        try:
            check=users.query.filter_by(id=user_id).first()
            if check is None:
                return "user not found",404
            s=scores.query.filter_by(id=user_id).all()
            if s is []:
                return "Yet to be reviewed",404
            res=[]
            for i in s:
                res.append({"deck_id": i.deck_id,"score": i.score})
            return res,200
        except:
            return "Internal Server Error",500
