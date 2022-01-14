from flask import Flask, request,session,redirect,url_for
from flask import render_template
from datetime import datetime
import pytz
from flask import current_app as app
from application.models import *
a={'!','#','$','%','/','^','&','*','>','<','{','}',']','[',"'",'"',",",'-',"|",'~',"`"}
@app.route("/",methods=["POST","GET"])
def hello():
    if request.method=="POST":
        _username=request.form.get("username")
        _password=request.form.get("password")
        if(_username==None or _password==None):
            return render_template("index.html")
        
        for i in _username:
            if i  in a:
                return render_template("index.html",error="Don't use symbols other than @,_ ")
        for j in _password:
            if j in a:
                return render_template("index.html",error="Don't use symbols other than @,_ ")
        check=users.query.filter_by(name=_username,password=_password).first()
        if check is None:
            return render_template("index.html",error="invalid username or password")
        session["user_id"]=check.id
        return redirect(url_for("home"))
    return render_template("index.html")

# logout 

@app.route('/logout')
def logout():
   session.pop("user_id", None)
   return redirect(url_for('hello'))

# dashboard

@app.route("/dashboard")
def home():
    if "user_id" not in session:
      return redirect(url_for('hello'))
    s=decks.query.all()
    outer=[]
    for i in s:
        q=scores.query.filter_by(deck_id=i.deck_id,id=session["user_id"]).first()
        t=cards.query.filter_by(deck_id=i.deck_id).all()
        if q is None:
            inner=[i.deck_name,0,"yet to be reviewed",i.deck_id,len(t)]
            outer.append(inner)
        else:
            inner=[i.deck_name,q.score,q.time,i.deck_id,len(t)]
            outer.append(inner)
    return render_template("dashboard.html",values=outer)
# b for score calculation 
b=[]

# deck_review

@app.route("/<deck_id>/review",methods=["GET","POST"])
def review(deck_id):
  if "user_id" not in session:
    return redirect(url_for('hello'))
  q=cards.query.filter_by(deck_id=deck_id).all()
  if request.method=="GET":
    session["count"]=1
    return render_template("review.html",card=q[session["count"]-1])
  if request.method=="POST":
    b.append(int(request.form["rating"]))
    print(b)
    session["count"]+=1
    if session["count"]<len(q):
      return render_template("review.html",card=q[session["count"]-1])
    else:
      print(b)
      mark=round((sum(b)/(3*(len(b))))*100)
      tz= pytz.timezone('Asia/Kolkata') 
      x=datetime.now(tz)
      result=str(x.strftime("%d"))+" "+str(x.strftime("%b"))+" "+str(x.strftime("%Y"))+" "+str(x.strftime("%I"))+":"+str(x.strftime("%M"))+" "+str(x.strftime("%p"))
      a=scores.query.filter_by(id=session["user_id"],deck_id=deck_id).first()
      if a is None:
          buff=scores(deck_id,session["user_id"],mark/2,result)
          db.session.add(buff)
          db.session.commit()
      else:
          a.time=result
          a.score=round(((a.score)+mark)/2)
          db.session.commit()
      b.clear()
      return render_template("result.html",result=mark)

# deck_management

@app.route("/deck_management")
def manage():
  if "user_id" not in session:
    return redirect(url_for('hello'))
  q=decks.query.all()
  return render_template("management.html",values=q,error=None)

#deck deletion

@app.route("/<deck_id>/delete")
def delete(deck_id):
  if "user_id" not in session:
    return redirect(url_for('hello'))
  s=decks.query.filter_by(deck_id=deck_id).first()
  t=cards.query.filter_by(deck_id=deck_id).all()
  e=scores.query.filter_by(deck_id=deck_id,id=session["user_id"]).first()
  for i in t:
      db.session.delete(i)
  db.session.delete(s)
  if e:
    db.session.delete(e)
  db.session.commit()
  q=decks.query.all()
  return render_template("management.html",values=q)

#deck update

@app.route("/<deck_id>/update",methods=["POST"])
def update(deck_id):
  if "user_id" not in session:
    return redirect(url_for('hello'))
  if request.method=="POST":
      s=decks.query.filter_by(deck_id=deck_id).first()
      t=request.form.get("deck_name")
      if(t==""):
          return "",410
      
      for i in t:
          if i  in a:
              return "",408
      check=decks.query.filter_by(deck_name=t).first()
      if(check is not None):
          return "",409
      s.deck_name=t
      db.session.commit()
      return "",200
  #s=decks.query.filter_by(deck_name=deck_name).first()

#card management

@app.route("/<deck_id>/card_management")
def card_management(deck_id):
  if "user_id" not in session:
    return redirect(url_for('hello'))
  q=cards.query.filter_by(deck_id=deck_id).all()
  return render_template("cards.html",values=q,deck_id=deck_id)

#card deletion

@app.route("/<deck_id>/cards/<card_id>/delete")
def card_delete(deck_id,card_id):
  if "user_id" not in session:
    return redirect(url_for('hello'))
  q=cards.query.filter_by(deck_id=deck_id,card_id=card_id).first()

  db.session.delete(q)
  db.session.commit()
  return redirect("/"+deck_id+"/card_management")

#card updation

@app.route("/<deck_id>/card/<card_id>/update",methods=["POST"])
def card_update(deck_id,card_id):
  if "user_id" not in session:
    return redirect(url_for('hello'))

  if request.method=="POST":
      q=cards.query.filter_by(deck_id=deck_id,card_id=card_id).first()
      front=request.form.get("front")
      back=request.form.get("back")
      if(front=="" or back==""):
          return "",410
      
      for i in front:
          if i  in a:
              return "",408
      for j in back:
          if j in a:
              return "",408
      q.front=front
      q.back=back
      db.session.commit()
      return "ok",200


# new card

@app.route("/<deck_id>/new_card",methods=["GET","POST"])
def new_card(deck_id):
  if "user_id" not in session:
    return redirect(url_for('hello'))
  if request.method=="POST":
      front=request.form.get("front")
      back=request.form.get("back")
      if(front=="" or back==""):
          return render_template("form.html",error="Empty input found")
      
      for i in front:
          if i  in a:
              return render_template("form.html",error="Invalid input")
      for j in back:
          if j in a:
              return render_template("form.html",error="Invalid input")
      s=cards(deck_id,front,back)
      db.session.add(s)
      db.session.commit()
      return redirect("/"+deck_id+"/card_management")
  return render_template("form.html")


#new deck

@app.route("/new_deck",methods=["GET","POST"])
def new_deck():
  if "user_id" not in session:
    return redirect(url_for('hello'))
  if request.method=="GET":
    return render_template("form2.html")
  if request.method=="POST":
      name=request.form.get("deck_name")
      if(name==None):
          return render_template("form2.html",error="empty input")
      
      for i in name:
          if i  in a:
              return render_template("form2.html",error="invalid input")
      check=decks.query.filter_by(deck_name=name).first()
      if(check is not None):
          return render_template("form2.html",error=" deck_name already  in use")
      s=decks(name)
      db.session.add(s)
      db.session.commit()
      return redirect("/deck_management")
