from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    age = None
    error = None

    if request.method == "POST":
        birth_year = int(request.form["birth_year"])
        current_year = datetime.now().year

        if birth_year > current_year or birth_year < 1900:
            error = "Please enter a valid birth year."
        else:
            age = current_year - birth_year

    return render_template(
        "index.html",
        age=age,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)