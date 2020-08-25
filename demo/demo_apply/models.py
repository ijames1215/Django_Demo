# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Testdb(models.Model):
    no = models.TextField(db_column='No', blank=True, primary_key=True)  # Field name made lowercase.
    gender = models.TextField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    math_score = models.IntegerField(db_column='Math_Score', blank=True, null=True)  # Field name made lowercase.
    eng_score = models.IntegerField(db_column='ENG_Score', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testdb'
