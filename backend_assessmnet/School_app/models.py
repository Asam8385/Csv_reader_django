from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=100)

class Class(models.Model):
    name = models.CharField(max_length=100)

class AssessmentArea(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    student_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Answers(models.Model):
    answer = models.CharField(max_length=100)

class Awards(models.Model):
    name = models.CharField(max_length=100)

class Subject(models.Model):
    subject = models.CharField(max_length=100)
    subject_score = models.FloatField()

class CorrectAnswers(models.Model):
    correctanswer = models.CharField(max_length=100)

class Summary(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    sydney_participant = models.CharField(max_length=100)
    sydney_percentile = models.FloatField()
    assessment_area = models.ForeignKey(AssessmentArea, on_delete=models.CASCADE)
    award = models.ForeignKey(Awards,on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.FloatField()
    student_score = models.FloatField()
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    participant = models.IntegerField()
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    Category_Id = models.TextField()
    Year_level_name = models.IntegerField()
    answer = models.ForeignKey(Answers,on_delete=models.CASCADE)
    Correct_answer = models.ForeignKey(CorrectAnswers,on_delete=models.CASCADE) 





