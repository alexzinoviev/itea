from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
#@app.route('/<name>')
def index(name='Anonymus'):
    #return render_template('index.html', name=name)
    db = sqlite3.connect('blog.db')
    cursor = db.execute('select * from posts order by id desc')
    posts = cursor.fetchall()
    db.close()
    return render_template('index.html', posts=posts)

@app.route('/add/', methods = ['GET', 'POST'])
def add():
    name = post = ''
    if request.method == 'POST':
        post = request.form.get('post', '')
        name = request.form.get('name', '')
        if post and name:
            db = sqlite3.connect('blog.db')
            db.execute('insert into posts (name, post) values (?,?)', (name, post))
            db.commit()
            #return redirect('/')
        #print(request.form['post'], request.form['name'])
    return render_template('add.html', name=name, post=post)

if __name__ == '__main__':
    app.run(debug=True)