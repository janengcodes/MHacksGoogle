import flask
import questopia
from questopia.views.quiz import correct_answers, questions

score = None  # Initialize score as a global variable

@questopia.app.route('/completion', methods=['POST'])
def show_results():
    global score  # Declare score as a global variable within the function
    answers = []
    wrong_questions = {}
    for question in flask.request.form:
        answers.append(flask.request.form[question])

    wrong = 0
    for i in range(len(correct_answers)):
        if correct_answers[i] != answers[i]:
            wrong += 1
            wrong_questions[questions[i]] = correct_answers[i]
    print(correct_answers)
    print(answers)

    correct = len(correct_answers) - wrong

    context = {"correct": correct, 
                "total": len(correct_answers),
                "incorrect": wrong_questions
            }
    if len(correct_answers) == 0:
        score = 0
    else:
        score = correct / len(answers)
    
    return flask.render_template("completion.html", **context)

@questopia.app.route('/portal',  methods=['GET'])
def show_portal():
    global score  # Declare score as a global variable within the function
    print(score)
    if score > 0.5:
        return flask.render_template("open_portal.html")
    return flask.render_template("closed_portal.html")
