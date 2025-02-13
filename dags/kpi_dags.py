import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from script.cron.summarize_kpi_data import summarize_kpi_data


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 10),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="kpi",
    default_args=default_args,
    description="kpi",
    schedule="00 08 07 * *",
    catchup=False,
    tags=["kpi"],
):
    t = PythonOperator(
        task_id='summarize_kpi_data',
        python_callable=summarize_kpi_data
    )
