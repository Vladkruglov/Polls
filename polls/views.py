from polls.polls.models import Question
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    context={"Questions":models.Question.objects.all()}
    g=models.Question.objects.first()
    con={"Choices":g.choice_set.all()}
    return render(request, "questions.html", context, con)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)