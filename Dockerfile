FROM python:3.9

# Instalar dependencias de Airflow
RUN pip install apache-airflow
RUN pip install -r requirements.txt

# Copiar archivos DAG al directorio de Airflow
COPY dags/ /usr/local/airflow/dags/
COPY .env  /

USER airflow

RUN pip install yfinance
RUN pip install psycopg2-binary
RUN pip install sendgrid

WORKDIR /usr/local/airflow
