"""
quest index (main) view.

URLs include:
/
"""
import flask
import questopia
from questopia.views.quiz import correct_answers, questions

score = 0.1 

@questopia.app.route('/completion', methods=['POST'])
def show_results():
    answers = []
    wrong_questions = {}
    for question in flask.request.form:
        answers.append(flask.request.form[question])

    # maybe show what question the kid got wrong
    wrong = 0
    for i in range(len(correct_answers)):
        if correct_answers[i] != answers[i]:
            wrong+=1
            wrong_questions[questions[i]] = correct_answers[i]
    print(correct_answers)
    print(answers)

    correct = len(correct_answers) - wrong

    # for response in answers:
    #     for correct_ans in correct_answers:

    context = {"correct": correct, 
                "total": len(correct_answers),
                "incorrect": wrong_questions
            }

    score = correct/len(correct_answers)
    
    return flask.render_template("completion.html", **context)

@questopia.app.route('/portal')
def open_portal():
    context = {}
    if (score > 0.5):
        return flask.render_template("open_portal.html", **context)
    return flask.render_template("closed_portal.html", **context)

