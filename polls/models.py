from django.db import models


class Question(models.Model):
    question_text_one = models.CharField(max_length=200)
    question_text_two = models.CharField(max_length=200)
    question_text_three = models.CharField(max_length=200)
    question_text_four = models.CharField(max_length=200)
    question_text_five = models.CharField(max_length=200)
    question_text_six = models.TextField()
    confirmation = models.BooleanField(default=True)
    second_confirmation = models.BooleanField(default=False)
    test_file = models.FileField()