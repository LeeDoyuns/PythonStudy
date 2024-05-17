from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=300, default='')
    pub_date = models.DateTimeField('date published', default=timezone.now)
    
    def __str__(self):
        return 'question_text = {}, pub_date = {}'.format(self.question_text, self.pub_date)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def __str__(self): 
        return 'question_id = {}, choice_text = {}, votes = {}'.format(self.question, self.choice_text, self.votes)
