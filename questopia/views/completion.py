"""
quest index (main) view.

URLs include:
/
"""
import flask
import questopia
from questopia.views.quiz import correct_answers, questions

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

    
    return flask.render_template("completion.html", **context)

