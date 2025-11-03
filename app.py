from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    # Zweck: Eingaben aus dem Textfeld entgegennehmen und wieder anzeigen.
    response = None
    if request.method == "POST":
        response = request.form.get("user_input", "")

    return render_template("index.html", title="Bachelorproject", response=response)

if __name__ == "__main__":
    app.run(debug=True)