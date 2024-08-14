# -*- coding: utf-8 -*-
"""PDA.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GWdMJKKB1Xq2AqdoFF4K5qbrBiPGiqe0
"""

!pip install tabula-py

"""Two dataset have been providing to extract data and one data is in pdf form. hence, !pip install tabula-py is used to import the pdf file in the software package tool."""

import tabula
from tabula.io import read_pdf

"""The above basic library helps in reading the provided pdf file


"""

import pandas as pd
from numpy import *
import numpy as np
import seaborn as sns
from tabula.io import convert_into
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

"""Seaborn and Matplotlib have been used to visualise the dataset. Panda has been used to import the essential excel file and numpy has been used to preserve the numerical calculation.

# Task 1: Loan Data Automation
"""

apex_pdf1 = tabula.io.read_pdf("APEX_Loans_Database_Table.pdf", pages='all')[0]   #importing pdf file in the software tool

tabula.convert_into("APEX_Loans_Database_Table.pdf", "pdf_apex.csv", output_format="csv", pages='all')   #convert the loan pdf into csv format

apex1_pdf = pd.read_csv('pdf_apex.csv')   #Importing the converted csv file

apex1_excel = pd.read_excel('APEX Loan Data.xlsx')   #import the excel file in the software tool

apex1_pdf.head()   #showing few rows of the pdf dataset

apex1_pdf.info()

apex1_excel.head()

apex1_excel.info()

"""#Merging the excel and pdf data"""

apex1_marge = [apex1_pdf, apex1_excel]
apex1_marge_loan = pd.concat(apex1_marge)

apex1_marge_loan.info()

"""#Checking duplicate values in the dataset


"""

sum(apex1_marge_loan.duplicated())

"""#Solving the duplicate values"""

apex1_merged_data=apex1_marge_loan.drop_duplicates()

apex1_merged_data.isnull().sum()

apex1_merged_data.to_csv('apex1_merged_data.csv', index=False)

"""#Descriptive statistics"""

apex1_merged_data.describe()

"""#Identifying the outliers of the dataset"""

fig = plt.figure(figsize =(18, 6))
sns.boxplot(apex1_merged_data,color="RED")
plt.show()

"""#Determining the data distribution of loan amount


"""

import plotly.express as px
fig = px.histogram(apex1_merged_data, x='LoanAmount', color_discrete_sequence=['pink'], title="Loan Amount Distribution")
fig.update_traces(marker_line_color='blue', marker_line_width=1.5)
fig.show()

"""#Data Visualisation"""

import plotly.express as px
fig = px.histogram(apex1_merged_data, x='Loan_Status', color='Loan_Status', color_discrete_sequence=px.colors.sequential.Plasma, title="Loan Status Count")
fig.update_traces(marker_line_color='black', marker_line_width=1.5)
fig.show()

import plotly.express as px
fig = px.histogram(apex1_merged_data, x='Loan_Status', color='Married', barmode='group',
                   color_discrete_sequence=px.colors.qualitative.Pastel,
                   title="Loan Status Count by Marriage Status")
fig.update_traces(texttemplate='%{y}', textposition='outside')
fig.update_traces(marker_line_color='black', marker_line_width=1.5)
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()

import plotly.express as px
fig = px.histogram(apex1_merged_data, x='Loan_Status', color='Dependents', barmode='group',
                   color_discrete_sequence=px.colors.sequential.Viridis,
                   title="Loan Status Count by Number of Dependents")
fig.update_traces(texttemplate='%{y}', textposition='outside')
fig.update_traces(marker_line_color='black', marker_line_width=1.5)
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()

"""# Task 2: Descriptive Analysis

1. Calculating the total amount loaned by AFS
"""

apex1_total_loan_amount = apex1_merged_data["LoanAmount"].sum()
print("Calculating the total loan amount of AFS is :\n",apex1_total_loan_amount)

"""2. Calculating the average amount loaned"""

apex1_avg_loan = apex1_merged_data["LoanAmount"].mean()
print("The Average loan amount of AFS is:\n", apex1_avg_loan)

"""3. Calculation for the average loan term"""

apex1_loan_avg_term = apex1_merged_data["Loan_Amount_Term"].mean()
print("Calculating the average loan term of AFS:", apex1_loan_avg_term)

"""4. The total number of applicants broken down into Approved and Rejected, the number of males and female in each case"""

apex1_approaval_loan_applicant=apex1_merged_data[apex1_merged_data["Loan_Status"]=='Y']
apex1_approaval_loan_applicant=apex1_approaval_loan_applicant["Loan_Status"].count()
print("Approval loan applicant:\n",apex1_approaval_loan_applicant)
apex1_rejected_loanapplicant=apex1_merged_data[apex1_merged_data["Loan_Status"]=='N']
apex1_rejected_loanapplicant=apex1_rejected_loanapplicant["Loan_Status"].count()
print("Rejected loan applicants:\n",apex1_rejected_loanapplicant)

import plotly.express as px
fig = px.histogram(apex1_merged_data, x='Loan_Status', color='Gender', barmode='group',
                   color_discrete_sequence=px.colors.sequential.Plasma,
                   title="Loan Status Count by Gender")
fig.update_traces(texttemplate='%{y}', textposition='outside')
fig.update_traces(marker_line_color='black', marker_line_width=1.5)
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide')
fig.show()

"""5. The maximum and minimum of amounts loaned"""

import plotly.express as px
labels = ['Maximum of loan amount', 'Minimum of loan amount']
values = [apex1_merged_data["LoanAmount"].max(), apex1_merged_data["LoanAmount"].min()]
fig = px.pie(names=labels, values=values,
             color=labels, color_discrete_sequence=px.colors.qualitative.Pastel,
             title="Maximum and Minimum Loan Amounts")
fig.update_traces(textinfo='label+value', textfont_size=15,
                  marker=dict(line=dict(color='black', width=2)))
fig.update_layout(showlegend=False)
fig.show()

"""6. The number of self-employed who had their loan approved, expressed as a percentage of all who had their loan approved"""

apex1_self_employed=apex1_merged_data[apex1_merged_data['Self_Employed']==1]
self_employed_apex_approved=apex1_self_employed[apex1_self_employed['Loan_Status'] == 'Y']
approved_loan=apex1_merged_data[apex1_merged_data['Loan_Status'] == 'Y']

self_employed_apex_approved_percent = (len(self_employed_apex_approved) / len(approved_loan)) * 100 if len(approved_loan) > 0 else 0
others_applicant_apex = 100 - self_employed_apex_approved_percent

apex1_new= {'details_self_employed_apex': ['Approved Loan and Self-employed', 'Other Applicants'], 'percentage_approved_apex': [self_employed_apex_approved_percent, others_applicant_apex]}
percentages = pd.DataFrame(apex1_new)

import plotly.express as px
fig = px.bar(percentages,
             x='details_self_employed_apex',
             y='percentage_approved_apex',
             title='The number of self-employed who had their loan approved, expressed as a percentage of all who had their loan approved',
             labels={'details_self_employed_apex': 'Details Self Employed', 'percentage_approved_apex': 'Percentage Approved'},
             color='percentage_approved_apex',
             color_continuous_scale=px.colors.sequential.Viridis)
fig.update_traces(texttemplate='%{y}', textposition='outside')
fig.update_traces(marker_line_color='black', marker_line_width=1.5)
fig.update_layout(uniformtext_minsize=8, uniformtext_mode='hide',
                  yaxis_title='Value',
                  xaxis_title='Details Self Employed',
                  height=500, width=700,
                  showlegend=False)
fig.show()

"""7. The income distribution of all main applicants, showing average and standard deviation"""

apex1_income=apex1_merged_data['ApplicantIncome']
sns.histplot(x=apex1_merged_data['ApplicantIncome'], color="Violet", edgecolor='none')
plt.title("Income distribution of main applicants")
plt.axvline(apex1_income.mean(), color='green', linestyle='dotted', linewidth=1.5, label=f'Mean: {apex1_income.mean():.2f}')
plt.axvline(apex1_income.std(), color='blue', linestyle='dotted', linewidth=1.5, label=f'Std Dev: {apex1_income.std():.2f}')
plt.legend()
plt.show()

"""8. The top ten applicants by loan amount"""

apex1_merged_data.nlargest(n=10, columns=['LoanAmount'])

"""9. The distribution of properties (rural, urban etc) of all loan applicants"""

Wv=sns.countplot(x ='Property_Area', data = apex1_merged_data, palette='summer')
for label in Wv.containers:
    Wv.bar_label(label)