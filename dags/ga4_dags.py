import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from script.ga_data.ga4.get_content_data_from_bigquery import get_content_data_from_bigquery
from script.ga_data.ga4.get_video_data_from_bigquery import get_video_data_from_bigquery
from script.ga_data.ga4.get_game_data_from_bigquery import get_game_data_from_bigquery
from script.ga_data.ga4.get_cms_dashboard import get_cms_dashboard
from script.ga_data.ga4.get_ams_dashboard import get_ams_dashboard
from script.ga_data.ga4.send_feishu_msg import send_feishu_msg
from script.ga_data.ga4.get_cover_perf import get_cover_perf
from script.ga_data.ga4.get_cdn_alarm import get_cdn_alarm
from script.ga_data.ga4.get_mvp_data import get_mvp_data
from script.ga_data.ga4.get_project_return_user import get_project_return_user
from script.ga_data.ga4.get_high_cvr_lp import high_cvr_lp
from script.ga_data.ga4.get_high_cvr_lp_md import get_high_cvr_lp_md

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 10),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="ga_data9",
    default_args=default_args,
    description="ga_data 九点执行的",
    schedule="00 09 * * *",
    catchup=False,
    tags=["ga_data"],
):
    t9_1 = PythonOperator(
        task_id='get_content_data_from_bigquery',
        python_callable=get_content_data_from_bigquery
    )
    t9_2 = PythonOperator(
        task_id='get_video_data_from_bigquery',
        python_callable=get_video_data_from_bigquery
    )
    t9_3 = PythonOperator(
        task_id='get_game_data_from_bigquery',
        python_callable=get_game_data_from_bigquery
    )
    t9_4 = PythonOperator(
        task_id='get_cms_dashboard',
        python_callable=get_cms_dashboard
    )
    t9_5 = PythonOperator(
        task_id='get_ams_dashboard',
        python_callable=get_ams_dashboard
    )
    t9_6 = PythonOperator(
        task_id='send_feishu_msg',
        python_callable=send_feishu_msg
    )
    t9_7 = PythonOperator(
        task_id='get_cover_perf',
        python_callable=get_cover_perf
    )
    t9_8 = PythonOperator(
        task_id='get_cdn_alarm',
        python_callable=get_cdn_alarm
    )
    t9_9 = PythonOperator(
        task_id='get_mvp_data',
        python_callable=get_mvp_data
    )

    t9_1 >> t9_2 >> t9_3 >> t9_4 >> t9_5 >> t9_6

with DAG(
    dag_id="ga_data10",
    default_args=default_args,
    description="ga_data 十点执行的",
    schedule="00 10 * * *",
    catchup=False,
    tags=["ga_data"],
):
    t10_1 = PythonOperator(
        task_id='high_cvr_lp',
        python_callable=high_cvr_lp
    )

    t10_2 = PythonOperator(
        task_id='get_high_cvr_lp_md',
        python_callable=get_high_cvr_lp_md
    )

with DAG(
    dag_id="ga_data14",
    default_args=default_args,
    description="ga_data 十四点执行的",
    schedule="00 14 * * *",
    catchup=False,
    tags=["ga_data"],
):
    t14_1 = PythonOperator(
        task_id='get_project_return_user',
        python_callable=get_project_return_user
    )
