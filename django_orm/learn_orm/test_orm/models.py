from django.db import models


# Create your models here.

class TestTable(models.Model):
    int_field = models.IntegerField(default=0)
    char_field = models.CharField(max_length=200)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()


class TestTableV2(models.Model):
    int_field = models.IntegerField(primary_key=True)
    char_field = models.CharField(max_length=200)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
