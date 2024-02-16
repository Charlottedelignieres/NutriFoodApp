from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Product(models.Model):
    code = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    nutrition_grade = models.CharField(max_length=10)
    categories_tags_en = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    


