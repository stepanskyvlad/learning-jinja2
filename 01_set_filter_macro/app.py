from flask import Flask, render_template


app = Flask(__name__)

todos = [
    ("Get milk", False),
    ("Learn programming", True),
]


@app.route('/')
def hello_world():
    return render_template("home.html", todos=todos)


if __name__ == '__main__':
    app.run(debug=True)
