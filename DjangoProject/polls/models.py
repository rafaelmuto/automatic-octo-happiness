from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def __rpepr__(self):
        return f"Question({self.question_text}, {self.pub_date})"

    def was_published_recently(self):
        from django.utils import timezone
        return self.pub_date >= timezone.now() - timezone.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def __repr__(self):
        return f"Choice({self.choice_text}, {self.votes})"

