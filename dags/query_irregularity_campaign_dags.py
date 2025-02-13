import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from script.cron.campaign_validator import campaign_validator


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 13),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="campaign_validator",
    default_args=default_args,
    description="campaign_validator",
    schedule="05 2 * * *",
    catchup=False,
):
    t = PythonOperator(
        task_id='campaign_validator',
        python_callable=campaign_validator
    )
