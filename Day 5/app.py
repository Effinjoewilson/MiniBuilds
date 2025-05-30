from dotenv import load_dotenv
load_dotenv()

from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///todo.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

print("DB URI:", app.config['SQLALCHEMY_DATABASE_URI'])

# Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)
    done = db.Column(db.Boolean, default=False)

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            new_task = Todo(task=task)
            db.session.add(new_task)
            db.session.commit()
        return redirect(url_for('index'))

    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    if request.method == 'POST':
        updated_task = request.form.get('task')
        if updated_task:
            todo.task = updated_task
            db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', todo=todo)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True)
