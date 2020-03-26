# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class HScore(models.Model):
    user_id = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(default=0)


class TempCount(models.Model):
    user_id = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
    count = models.IntegerField(default=0)


class TableRender(models.Model):
    user_id = models.CharField(max_length=32)
    timestamp = models.DateTimeField(auto_now_add=True)
    table = models.CharField(max_length=200)