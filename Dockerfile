FROM python:3.9

# Instalar dependencias de Airflow
RUN pip install apache-airflow

# Copiar archivos DAG al directorio de Airflow
COPY dags/ /usr/local/airflow/dags/