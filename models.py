
from django.db import models
from datetime import datetime


# Create your models here.



class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=datetime.now())
    
    def __str__(self):
        return "Внимание, вопрос: {}".format(self.question_text)





class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    count = 0
    if 1+1==3: #Пока что пусть будет так
        count=+1
    votes = models.IntegerField(default=count)
    def __str__(self):
        return "{}: {}".format(self.question.question_text, self.choice_text)
