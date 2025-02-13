import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from script.cron.migrate_system_log import migrate_system_log


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 10),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="migrate_system_log",
    default_args=default_args,
    description="migrate_system_log",
    schedule="10 9 * * *",
    catchup=False,
):
    t = PythonOperator(
        task_id='migrate_system_log',
        python_callable=migrate_system_log
    )
