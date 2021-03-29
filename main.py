from flask import Flask, render_template, url_for, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:admin@localhost/sqlalchemy"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'LDFHSUFY8er283HEUHF092y3h4h'
db = SQLAlchemy(app)

menu = [{"name": "Главная", "url": "/"},
        {"name": "Войти", "url": "join"}]


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(30), unique=True, nullable=True)
    email = db.Column(db.String(50), unique=True, nullable=True)
    pwd = db.Column(db.String(200), nullable=True)
    date = db.Column(db.DateTime(200), default=datetime.utcnow)

    def __repr__(self):
        return f"<users {self.id}>"


@app.route("/")
def index():
    return render_template("index.html", menu=menu)


@app.route("/reg", methods=('POST', "GET"))
def reg():
    if request.method == 'POST':
        try:

            if request.form['pwd'] == request.form['pwd_check']:
                hash = generate_password_hash(request.form['pwd'])
                u = Users(email=request.form["email"], pwd=hash, login=request.form["login"])
                db.session.add(u)
                db.session.flush()
                db.session.commit()
                return render_template("profile.html", login=request.form["login"], menu=menu)
            else:
                print(f"Неправильний пароль")
        except:
            db.session.rollback()
            print(f"Помилка додавання в БД")
    return render_template("reg.html", menu=menu)


@app.route("/join", methods=('POST', "GET"))
def join():
    session.pop('userLogged', None)
    if 'userLogged' in session:
        return redirect(url_for('profile', email=session['userLogged']))
    elif request.method == 'POST':

        user = Users.query.filter_by(email=request.form["email"]).first()
        if not user is None:
            if check_password_hash(str(user.pwd), str(request.form["pwd"])):
                session['userLogged'] = request.form["email"]
                redirect(url_for('profile', email=session['userLogged']))
        else:
            flash("Неправильний логін або пароль")

    return render_template("join.html", menu=menu)


@app.route("/profile/<email>")
def profile(email):
    return render_template("profile.html", email=email, menu=menu)


if __name__ == "__main__":
    app.run(debug=True)
