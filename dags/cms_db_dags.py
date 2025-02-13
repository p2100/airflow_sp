import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from script.clickhouse.migrate_pgsql_to_clickhouse import migrate_pgsql_to_clickhouse


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 13),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="cms_db",
    default_args=default_args,
    description="cms db",
    schedule="20 00 * * *",
    catchup=False,
    tags=["cms_db"],
):
    t = PythonOperator(
        task_id='migrate_pgsql_to_clickhouse',
        python_callable=migrate_pgsql_to_clickhouse
    )
