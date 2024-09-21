from flask import render_template, send_from_directory, request
from website import create_app


app = create_app()


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/robots.txt")
def robots_txt():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route("/sitemap.xml")
def sitemap_xml():
    return send_from_directory(app.static_folder, request.path[1:])



if __name__ == "__main__":
    app.run()
