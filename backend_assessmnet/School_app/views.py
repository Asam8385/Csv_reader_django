# views.py

from django.shortcuts import render
from .models import School, Class, Subject, Answers, Summary, AssessmentArea, Awards, CorrectAnswers, Student
import pandas as pd

def visualize_data(request):
    path = './School_app/Ganison_dataset/Ganison_dataset_1.csv'
    data1 = pd.read_csv(path)

    path = './School_app/Ganison_dataset/Ganison_dataset_2.csv'
    data2 = pd.read_csv(path)

    path = './School_app/Ganison_dataset/Ganison_dataset_3.csv'
    data3 = pd.read_csv(path)

    path = './School_app/Ganison_dataset/Ganison_dataset_4.csv'
    data4 = pd.read_csv(path)

    path = './School_app/Ganison_dataset/Ganison_dataset_5.csv'
    data5 = pd.read_csv(path)

    path = './School_app/Ganison_dataset/Ganison_dataset_6.csv'
    data6 = pd.read_csv(path)

    combined_data = pd.concat([data1, data2, data3, data4, data5, data6], ignore_index=True)
    combined_data = combined_data.drop_duplicates()
    combined_data = combined_data.sample(n = 20)
    


    # Define the columns for each new DataFrame
    cols_school_year = ['school_name', 'year']
    cols_student_info = ['StudentID', 'First Name', 'Last Name']
    cols_class = ['Class']
    cols_assessment_area = ['Assessment Areas']
    cols_answers = ['Answers']
    cols_award = ['award']
    cols_subject = ['Subject']

    # Creating new DataFrames based on specified columns
    df_school_year = combined_data[cols_school_year]
    df_student_info = combined_data[cols_student_info]
    df_class = combined_data[cols_class]
    df_assessment_area = combined_data[cols_assessment_area]
    df_answers = combined_data[cols_answers]
    df_award = combined_data[cols_award]
    df_subject = combined_data[cols_subject]

    # Get the remaining columns not specifically grouped
    remaining_columns = [col for col in combined_data.columns if col not in (
        cols_school_year + cols_student_info + cols_class + 
        cols_assessment_area + cols_answers + cols_award + cols_subject
    )]
    
    # Create DataFrame for the remaining columns
    df_remaining = combined_data[remaining_columns]
    
    
    # Convert each DataFrame to HTML
    html_school_year = df_school_year.to_html(classes='table table-success table-hover', index=False)
    html_student_info = df_student_info.to_html(classes='table table-success table-hover', index=False)
    html_class = df_class.to_html(classes='table table-success table-hover', index=False)
    html_assessment_area = df_assessment_area.to_html(classes='table table-success table-hover', index=False)
    html_answers = df_answers.to_html(classes='table table-success table-hover', index=False)
    html_award = df_award.to_html(classes='table table-success table-hover', index=False)
    html_subject = df_subject.to_html(classes='table table-success table-hover', index=False)
    html_remaining = df_remaining.to_html(classes='table table-success table-hover', index=False)
    
    context = {
    'html_school_year': html_school_year,
    'html_student_info': html_student_info,
    'html_class': html_class,
    'html_assessment_area': html_assessment_area,
    'html_answers': html_answers,
    'html_award': html_award,
    'html_subject': html_subject,
    'html_remaining': html_remaining,
    }


    
    return render(request, './template/visualize_data.html', context )
#, {'schools': schools, 'classes': classes, 'subjects': subjects,'answers':answers,
#                                                   'summaries':summaries, 'assessmentArea':assessmentArea, 'awards':awards,'correctAnswers':correctAnswers,'students':students})
