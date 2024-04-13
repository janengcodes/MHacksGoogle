"""
quest index (main) view.

URLs include:
/
"""
import flask
import questopia

@questopia.app.route('/')
def show_index():
    """Display / route."""
    context = {}
    return flask.render_template("index.html", **context)

