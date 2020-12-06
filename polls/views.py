
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
    context={"Questions":models.Question.objects.all()}
    return render(request, "questions.html", context)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    question = models.Question.objects.get(pk=question_id)
    return render(request, "vote.html", {"question": question})

def make_vote(request):
    choice_id = request.GET.get('choice')
    choice = models.Choice.objects.get(pk=choice_id)
    choice.votes += 1
    choice.save()
    return HttpResponse("Вы успешно проголосовали за вопрос: {} !".format(models.Question.question_text()))