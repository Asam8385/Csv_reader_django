import os
import csv
from django.core.management.base import BaseCommand
from School_app.models import School, Student, Class, Subject, Answers, Summary, AssessmentArea, Awards, CorrectAnswers

class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        csv_files = [
            'Ganison_dataset_1.csv',
            'Ganison_dataset_2.csv',
            'Ganison_dataset_3.csv',
            'Ganison_dataset_4.csv',
            'Ganison_dataset_5.csv',
            'Ganison_dataset_6.csv'
        ]

        for file_name in csv_files:
            csv_file_path = os.path.join('E:\interview\Ganison_dataset', file_name)
            self.populate_table(csv_file_path)

    def populate_table(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                school, created = School.objects.get_or_create(name=row['school_name'])
                student, created = Student.objects.get_or_create(student_id=row['StudentID'], first_name=row['First Name'], last_name=row['Last Name'])
                class_instance, created = Class.objects.get_or_create(name=row['Class'])
                subject, created = Subject.objects.get_or_create(subject=row['Subject'],subject_score=row['average_score'])
                answers, created = Answers.objects.get_or_create(answer=row['Answers'])
                assessment_area, created = AssessmentArea.objects.get_or_create(name=row['Assessment Areas'])
                awards, created = Awards.objects.get_or_create(name=row['award'])
                correct_answers,created = CorrectAnswers.objects.get_or_create(correctanswer = row['Correct Answers'])

                Summary.objects.create(
                    school=school,
                    sydney_participant=row['sydney_participants'],
                    sydney_percentile=row['sydney_percentile'],
                    assessment_area=assessment_area,
                    award=awards,
                    class_name=class_instance,
                    correct_answer_percentage_per_class=row['correct_answer_percentage_per_class'],#
                    student=student,
                    participant=row['participant'],
                    student_score=row['student_score'],
                    subject=subject,
                    Year_level_name=row['Year Level'],
                    answer=answers,
                    Correct_answer=correct_answers,
                  
                )
