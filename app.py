from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        # Temporary login credentials
        if role == "student" and username == "student" and password == "1234":
            return "Welcome Student!"

        if role == "faculty" and username == "faculty" and password == "1234":
            return "Welcome Faculty!"

        return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)