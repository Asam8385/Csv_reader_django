# Generated by Django 5.0.3 on 2024-03-11 06:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AssessmentArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Awards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CorrectAnswers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correctanswer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('subject_score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Summary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sydney_participant', models.CharField(max_length=100)),
                ('sydney_percentile', models.FloatField()),
                ('correct_answer_percentage_per_class', models.FloatField()),
                ('student_score', models.FloatField()),
                ('participant', models.IntegerField()),
                ('Category_Id', models.TextField()),
                ('Year_level_name', models.IntegerField()),
                ('Correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_app.correctanswers')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_app.answers')),
                ('assessment_area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_app.assessmentarea')),
                ('award', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_app.awards')),
                ('class_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_app.class')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_app.school')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_app.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='School_app.subject')),
            ],
        ),
    ]
