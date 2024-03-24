from flask import Flask, redirect, render_template, request, jsonify
from loginform import LoginForm
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from data.users import User
from data.notes import Note
from forms.user import RegisterForm
from forms.newNoteForm import NoteAddingForm
from forms.delete import DeleteNote
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(name=form.name.data, email=form.email.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route("/", methods=['GET', 'POST'])
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        notes = db_sess.query(Note).filter(Note.user == current_user)
        add_form = NoteAddingForm()
        delete_form = DeleteNote()
        if add_form.validate_on_submit():
            user = db_sess.query(User).filter(User.email == current_user.email).first()
            note = Note(user_id=user.id, text=add_form.text.data, header=add_form.header.data)
            db_sess.add(note)
            db_sess.commit()
            return redirect('/')

    else:
        return redirect('/login')

    return render_template("index.html", notes=notes, add_form=add_form, delete_form=delete_form)


@app.route('/delete', methods=['POST'])
@login_required
def delete_note():
    req = request.form.getlist('id')
    note_id = req[0] if req[0] else req[1]
    db_sess = db_session.create_session()
    note = db_sess.query(Note).filter(Note.id == note_id).first()
    db_sess.delete(note)
    db_sess.commit()
    return redirect('/')


if __name__ == '__main__':
    db_session.global_init("db/notes.db")
    app.run(port=8080, host='127.0.0.1')

