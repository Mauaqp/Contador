from flask import Flask, render_template, request, redirect, session


app = Flask(__name__)
app.secret_key = "miclave"

#Route
@app.route('/')         
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session["count"] += 2
    return render_template("index.html")

#Route increment
@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

#App.run
if __name__ == "__main__":
    app.run(debug=True)