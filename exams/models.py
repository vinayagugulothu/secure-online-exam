from django.db import models
from django.conf import settings


class Exam(models.Model):

    title = models.CharField(max_length=200)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Question(models.Model):

    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)

    question_text = models.TextField()

    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)

    correct_option = models.CharField(max_length=10)

    def __str__(self):
        return self.question_text