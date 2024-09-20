from flask import Blueprint, render_template, request

from website.static._python.cases_scripts import to_sentence_case, to_title_case, to_capitalize_case

views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST", "PUT"])
def home():
    if request.method == "PUT":
        initial_text = request.form.get("initial_text")
        char_count = len(initial_text)
        if request.form.get("submit_upper") == "uppercase":
            initial_text = initial_text.upper()
        elif request.form.get("submit_lower") == "lowercase":
            initial_text = initial_text.lower()
        elif request.form.get("submit_capitalize") == "capitalize":
            initial_text = to_capitalize_case(initial_text)
        elif request.form.get("submit_title") == "title":
            initial_text = to_title_case(initial_text)
        elif request.form.get("submit_sentence") == "sentence":
            initial_text = to_sentence_case(initial_text)
        return render_template("_partials/text_response.html", initial_text=initial_text, char_count=char_count)
    return render_template("home.html")
