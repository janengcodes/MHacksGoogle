"""
quest quiz view.

URLs include:
/
"""
import flask
import questopia

quizDict = {}
# key = question, val = answer

# Adds question and ans to quiz dict
def quizzy(question, ans):
    quizDict[question] = ans
    print(question)
    print(quizDict[question])
    