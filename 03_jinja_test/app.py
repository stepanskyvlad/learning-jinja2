from flask import Flask, render_template


app = Flask(__name__)


def square(value):
    return (value ** 0.5).is_integer()


app.jinja_env.tests["square"] = square


@app.route("/")
def todo():
    return render_template("fizzbuzz.html")


if __name__ == "__main__":
    app.run(debug=True)
