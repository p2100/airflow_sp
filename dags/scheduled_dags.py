import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.append('project/')
from apps.modules.staff.timer import update_feishu_info, synchronization_point

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 19),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

update_feishu_info_dags = PythonOperator(
    task_id='update_feishu_info',
    python_callable=update_feishu_info,
    dag=DAG(
        'update_feishu_info',
        default_args=default_args,
        description='同步飞书员工信息',
        schedule_interval="7 23 * * *",
        catchup=False,
    ),
)

synchronization_point_dags = PythonOperator(
    task_id='synchronization_point',
    python_callable=synchronization_point,
    dag=DAG(
        'synchronization_point',
        default_args=default_args,
        description='积分兑换奖品',
        schedule_interval="*/2 * * * *",
        catchup=False,
    ),
)
