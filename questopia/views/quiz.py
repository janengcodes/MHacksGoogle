"""
quest quiz view.

URLs include:
/
"""
import flask
import questopia
import google.generativeai as genai
import random

# from questopia.views.env import model
GOOGLE_API_KEY = 'AIzaSyCGu2PKA-ly-HGgkuiyswIPoVIUo64M9b4'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.0-pro')
correct_answers = []
questions = []
quizDict = {} 
key = 0
# key = question, val = answer

# Adds question and ans to quiz dict
def quizzy(question, ans):
    global key
    
    num = random.random()
    if num < 0.4:
        response = model.generate_content("make a true or false question based on this text such that the answer is false, just return the question: "+ ans)
        output = response.text
        quizDict[key] = (output, 'false')
    else:
        response = model.generate_content("make a true or false question based on this text such that the answer is true, just return the question: "+ ans)
        output = response.text
        quizDict[key] = (output, 'true')
        
    print(quizDict[key][0], quizDict[key][1])
    key+=1

@questopia.app.route('/quiz')
def show_quiz():
    """Display / route."""
        
    for _, value in quizDict.items():
        questions.append(value[0])
        correct_answers.append(value[1])
        
    context = {
        "questions":questions,
    }
        
    return flask.render_template("quiz.html", **context)

