from flask import Flask, render_template

app = Flask(__name__)
a = ["Task no 1,", "Task no 2", "Task no 3"]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add task')
def add_task():
    < form
    action = "{{ url_for('ask') }}"
    method = "GET" ><form action="{{ url_for('add_task') }}" method="GET">
    return render_template('task')


if __name__ == '__main__':
    app.run(debug=True)
