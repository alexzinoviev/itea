from flask import Flask, render_template, request, redirect, session, g
import sqlite3

app = Flask(__name__)
app.secret_key = '!QAZ@WSX#EDC$RFV%TGB^YHN&UJM*IK<(OL>)P:_{'

@app.before_request
def before_request():
    g.db = sqlite3.connect('blog.db')
    g.message = session.pop('message', '')

@app.after_request
def after_request(f):
    g.db.close()
    return f


@app.route('/')
#@app.route('/<name>')
def index(name='Anonymus'):
    #return render_template('index.html', name=name)
    cursor = g.db.execute('select * from posts order by id desc')
    posts = cursor.fetchall()
    session['message'] = 'Add post'
    #message = session.pop('message', '')
    return render_template('index.html', posts=posts, message=g.message)

@app.route('/add/', methods = ['GET', 'POST'])
def add():
    name = post = ''
    if request.method == 'POST':
        post = request.form.get('post', '')
        name = request.form.get('name', '')
        if post and name:
            g.db.execute('insert into posts (name, post) values (?,?)', (name, post))
            g.db.commit()
            session['message'] = 'Post has been added succesfully'
            return redirect('/')
        #print(request.form['post'], request.form['name'])
    return render_template('add.html', name=name, post=post, message = g.message)

if __name__ == '__main__':
    app.run(debug=True)