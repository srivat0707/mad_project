from flask import Flask,render_template
app=Flask(__name__)
@app.route("/get")
def home():
    return render_template("form2.html")
if __name__ =="__main__":
    app.run()