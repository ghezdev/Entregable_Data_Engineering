
from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from etl import get_info_weather, clean_data, connect_to_redshift, insert_data_to_redshift

default_args = {
    'owner': 'Guillermo Hernández',
    'start_date': datetime(2024, 6, 5),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag_get_weather_data = DAG(
    dag_id='get_weather_data',
    default_args=default_args,
    description='get_weather_data',
    schedule_interval=timedelta(days=1),
    catchup=False
)


task_get_info_weather = PythonOperator(
    task_id='get_info_weather',
    python_callable=get_info_weather,
    dag=dag_get_weather_data,
)

task_clean_data = PythonOperator(
    task_id='clean_data',
    python_callable=clean_data,
    dag=dag_get_weather_data,
)

task_connect_to_redshift = PythonOperator(
    task_id='connect_to_redshift',
    python_callable=connect_to_redshift,
    dag=dag_get_weather_data,
)

task_insert_data_to_redshift = PythonOperator(
    task_id='insert_data_to_redshift',
    python_callable=insert_data_to_redshift,
    dag=dag_get_weather_data,
)


task_get_info_weather >> task_clean_data >> task_connect_to_redshift >> task_insert_data_to_redshift
