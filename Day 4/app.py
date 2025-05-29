from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

# In-memory list to store tasks
todos = []
next_id = 1


@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todos.append({
                'id': next_id,
                'task': task,
                'done': False
            })
            next_id += 1
        return redirect(url_for('index'))

    return render_template('index.html', todos=todos)


@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))


@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit(todo_id):
    todo = next((t for t in todos if t['id'] == todo_id), None)
    if not todo:
        return "Task not found", 404

    if request.method == 'POST':
        updated_task = request.form.get('task')
        if updated_task:
            todo['task'] = updated_task
        return redirect(url_for('index'))

    return render_template('edit.html', todo=todo)


if __name__ == '__main__':
    app.run(debug=True)
