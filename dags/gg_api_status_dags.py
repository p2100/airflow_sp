import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from script.cron.gg_api_status import gg_api_status


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 13),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="gg_api_status",
    default_args=default_args,
    description="gg_api_status",
    schedule="*/20 * * * *",
    catchup=False,
    tags=["gg_api_status"],
):
    t = PythonOperator(
        task_id='gg_api_status',
        python_callable=gg_api_status
    )
