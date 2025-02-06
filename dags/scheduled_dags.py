import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from apps.modules.staff.timer import update_feishu_info, synchronization_point
from apps.modules.mcc.timer import main as mcc_link

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 19),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

update_feishu_info_dag = DAG(
    'update_feishu_info',
    default_args=default_args,
    description='同步飞书员工信息',
    schedule_interval="7 23 * * *",
    catchup=False,
)

update_feishu_info_dags = PythonOperator(
    task_id='update_feishu_info',
    python_callable=update_feishu_info,
    dag=update_feishu_info_dag
)

synchronization_point_dag = DAG(
    'synchronization_point',
    default_args=default_args,
    description='积分兑换奖品',
    schedule_interval="*/2 * * * *",
    catchup=False,
)

synchronization_point_dags = PythonOperator(
    task_id='synchronization_point',
    python_callable=synchronization_point,
    dag=synchronization_point_dag
)

mcc_link_dag = DAG(
    'mcc_link',
    default_args=default_args,
    description='MCC Link轮询',
    schedule_interval="*/20 * * * *",
    catchup=False,
)

mcc_link_dags = PythonOperator(
    task_id='mcc_link',
    python_callable=mcc_link,
    dag=mcc_link_dag
)
