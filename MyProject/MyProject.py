import sqlite3
import os
from flask import Flask, render_template, flash, request, g, abort

from fdatabase import FDataBase

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'kjdfkreg5f4hf4s5f4gn8f7gn45xf4b5d4n5fg'
# конфигурация
DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'ba92ab4e8b8755797efef56a86d6698e91db0ffc'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, "flsk.db")))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():  # сейчас в коде не участвует
    db = connect_db()
    with app.open_resource("sq_db.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.route("/")
def index():
    db = get_db()
    dbase = FDataBase(db)
    return render_template('index.html', menu=dbase.get_menu(), posts=dbase.get_posts_anonce())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDataBase(db)

    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["post"]) > 10:
            res = dbase.add_post(request.form["name"], request.form["post"])
            if not res:
                flash("Ошибка добавления статьи", category="error")
            else:
                flash("Статья добавлена успешно", category="success")
        else:
            flash("Ошибка добавления статьи", category="error")

    return render_template('add_post.html', menu=dbase.get_menu())


@app.route("/post/<int:id_post>")
def show_post(id_post):
    db = get_db()
    dbase = FDataBase(db)
    title, post = dbase.get_post(id_post)
    if not title:
        abort(404)

    return render_template('post.html', menu=dbase.get_menu(), title=title, post=post)


@app.errorhandler(404)
def page_not_found(error):
    db = get_db()
    dbase = FDataBase(db)
    return render_template("page404.html", title="Страница не найдена", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()

# menu = [
#     {"name": "Главная", "url": "index"},
#     {"name": "О нас", "url": "about"},
#     {"name": "Услуги", "url": "services"},
#     {"name": "Наши контакты", "url": "address"},
#     {"name": "Обратная связь", "url": "contact"}
# ]
#
#
# @app.route("/index")
# def index():
#     return render_template("index.html", title="Главная", menu=menu)
#
#
# @app.route("/about")
# def about():
#     return render_template("about.html", title="О нас", menu=menu)
#
# @app.route("/services")
# def services():
#     return render_template("services.html", title="Услуги", menu=menu)
#
# @app.route("/address")
# def address():
#     return render_template("address.html", title="Наши контакты", menu=menu)
#
# @app.route("/contact", methods=["POST", "GET"])
# def contact():
#     if request.method == "POST":
#         # print(request.form)
#         # print(request.form['username'])
#         if len(request.form['username']) > 2:
#             flash("Сообщение отправлено успешно!", category='success')
#         else:
#             flash("Ошибка отправки", category='error')
#     return render_template("contact.html", title="Обратная связь", menu=menu)
# # int - должны присутствовать только цифры
# # float - может записываться число с плавающей точкой
# # path - можно использовать любые допустимые символы URL плюс символ слеша("/")
#
# @app.route("/profile/<path:username>")
# def profile(username):
#     return f"Пользователь: {username}"
#
#
# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template("page404.html", title="Страница не найдена", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)






