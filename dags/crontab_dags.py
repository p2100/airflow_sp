import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from script.cron.mongo_material_adids_to_casbin import mongo_material_adids_to_casbin
from script.cron.scan_local_cover import scan_local_cover
from script.cron.cdn_alarm import cdn_alarm
from script.cron.cdn_alarm_301 import cdn_alarm_301
from script.cron.cdn_alarm_doc import cdn_alarm_doc


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 13),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="mongo_material_adids_to_casbin",
    default_args=default_args,
    description="mongo_material_adids_to_casbin",
    schedule="00 09 * * *",
    catchup=False,
):
    t1 = PythonOperator(
        task_id='mongo_material_adids_to_casbin',
        python_callable=mongo_material_adids_to_casbin
    )

with DAG(
    dag_id="scan_local_cover",
    default_args=default_args,
    description="scan_local_cover",
    schedule="*/10 * * * *",
    catchup=False,
):
    t2 = PythonOperator(
        task_id='scan_local_cover',
        python_callable=scan_local_cover
    )
    t3 = PythonOperator(
        task_id='cdn_alarm',
        python_callable=cdn_alarm
    )
    t4 = PythonOperator(
        task_id='cdn_alarm_301',
        python_callable=cdn_alarm_301
    )

with DAG(
    dag_id="cdn_alarm_doc",
    default_args=default_args,
    description="cdn_alarm_doc",
    schedule="*/30 * * * *",
    catchup=False,
):
    t5 = PythonOperator(
        task_id='cdn_alarm_doc',
        python_callable=cdn_alarm_doc
    )

