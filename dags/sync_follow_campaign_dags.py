import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from script.cron.sync_follow_campaign import sync_follow_campaign


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 13),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="sync_follow_campaign",
    default_args=default_args,
    description="sync_follow_campaign",
    schedule="30 2 * * *",
    catchup=False,
):
    t = PythonOperator(
        task_id='sync_follow_campaign',
        python_callable=sync_follow_campaign
    )
