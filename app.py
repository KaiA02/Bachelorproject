from flask import Flask, render_template, request

from wiki_api import get_wikipedia_article_from_prompt
from thePile_api import get_chatgpt_answer_from_prompt

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    user_input = ""
    response = None
    engine = None

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        lower = user_input.lower()

        # ENTSCHEIDUNG NUR ÜBER "from ..."
        if "from wikipedia" in lower:
            engine = "wikipedia"
            response = get_wikipedia_article_from_prompt(user_input)

        elif "from chatgpt" in lower or "from pile" in lower:
            engine = "chatgpt / the pile"
            response = get_chatgpt_answer_from_prompt(user_input)

        else:
            engine = "unknown"
            response = (
                "Reference unknown. Use e.g. 'from wikipedia' or 'from chatgpt' (aka the Pile)."
            )

    return render_template(
        "index.html",
                           title="Bachelorproject",
                           response=response,
                           user_input=user_input,
                           engine=engine)

if __name__ == "__main__":
    app.run(debug=True)