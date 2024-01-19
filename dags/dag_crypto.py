from script_crypto import get_crypto_data
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Rodrigo',
    # Empieza a ejecutarse desde el dia de la entrega
    'start_date': datetime(2024, 1, 15),
    # En caso falle, intenta 3 vez mas 
    'retries': 3,
    # El tiempo de espera es de 5 min
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='crypto_data_dag',
    default_args=default_args,
    description='DAG para obtener datos de criptomonedas y cargar en base de datos',
    schedule_interval=timedelta(hours=12),  # Frecuencia de ejecución
)

run_task = PythonOperator(
    task_id='run_crypto_data_task',
    python_callable= get_crypto_data,
    dag=dag
)

run_task