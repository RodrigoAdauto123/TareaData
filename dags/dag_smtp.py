from datetime import datetime
from email import message
from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator
import smtplib

def enviar():
    senderEmail = Variable.get("senderEmail")
    senderPasswordEmail = Variable.get("senderPasswordEmail")
    receiberEmail = Variable.get("receiberEmail")
    subjectMessaje = Variable.get("subjectMessaje")
    bodyMessaje = Variable.get("bodyMessaje")

    x=smtplib.SMTP('smtp.gmail.com',587)
    x.starttls()
    x.login(senderEmail,senderPasswordEmail)
    subject=subjectMessaje
    body_text=bodyMessaje
    message='Subject: {}\n\n{}'.format(subject,body_text)
    x.sendmail(senderEmail, receiberEmail, message)
    print('Exito')

default_args={
    'owner': 'RodrigoA',
    'start_date': datetime(2024,2,1)
}

with DAG(
    dag_id='dag_smtp_email_automatico',
    default_args=default_args,
    schedule_interval='@daily') as dag:

    tarea_1=PythonOperator(
        task_id='dag_envio',
        python_callable=enviar
    )

    tarea_1