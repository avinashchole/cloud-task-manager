from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL Database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="taskdb",
    use_pure=True
)


@app.route('/')
def index():
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template("index.html", tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    cursor = db.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (%s)", (task,))
    db.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_task(id):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
