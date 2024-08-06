# news_etl_dag.py
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from reddit_etl import etl_process  

# Define default_args and the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'news_etl_dag',
    default_args=default_args,
    description='A simple ETL DAG for fetching news and uploading to S3',
    schedule_interval='@daily',  # Adjust as needed
    start_date=days_ago(1),
    catchup=False,
)

# Define the task
etl = PythonOperator(
    task_id='fetch_and_upload_news',
    python_callable=etl_process,
    dag=dag,
)