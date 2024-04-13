import flask
import questopia
import google.generativeai as genai
from questopia.views.quiz import quizzy

GOOGLE_API_KEY = 'AIzaSyCGu2PKA-ly-HGgkuiyswIPoVIUo64M9b4'

model = None

def initialize_generative_model(character):
    """Initialize the GenerativeModel with the specified character."""
    global model
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel(
        "models/gemini-1.5-pro-latest",
        system_instruction="you are a history expert that talks like " + character + " and your name is " + character,
    )

@questopia.app.route('/env')
def show_env():
    """Display main index view."""
    # model = genai.GenerativeModel(
    #     "models/gemini-1.5-pro-latest",
    #     system_instruction="you are a history expert that talks like yoda",
    # )
    # print(response.text)
    return flask.render_template("env.html")


@questopia.app.route('/env', methods=['POST'])
def show_env_post():
    """Display main index view."""
    character = flask.request.form['character']
    print(character)
    initialize_generative_model(character)

    return flask.render_template("env.html")

@questopia.app.route('/process_question', methods=['POST'])
def process_question():
    """Process the question submitted from the form."""

    question = flask.request.form['question']
    print(question)
    output = ""
    if question:
        if model:
            response = model.generate_content(question)
            output = response.text
            print(response.text)

    quizzy(question, output)
    return flask.render_template("env.html", output_from_flask=output)
