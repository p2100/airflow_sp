import sys
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

sys.path.insert(0, 'project/')
from script.cron.grafana_analytics_data.get_campaign import get_campaign
from script.cron.grafana_analytics_data.get_campaign_cost import get_campaign_cost
from script.cron.grafana_analytics_data.get_single_campaign_cost import get_single_campaign_cost
from script.cron.grafana_analytics_data.ga_data import ga_data
from script.cron.grafana_analytics_data.get_suffix_category import get_suffix_category


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 10),
    'retries': 0,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id="grafana_analytics_get_campaign",
    default_args=default_args,
    description="grafana_analytics_get_campaign",
    schedule="10 0 * * *",
    catchup=False,
    tags=["grafana_analytics"],
):
    t1 = PythonOperator(
        task_id='grafana_analytics_get_campaign',
        python_callable=get_campaign
    )

with DAG(
    dag_id="grafana_analytics_get_campaign_cost",
    default_args=default_args,
    description="grafana_analytics_get_campaign_cost",
    schedule="00 8 * * *",
    catchup=False,
    tags=["grafana_analytics"],
):
    t2 = PythonOperator(
        task_id='grafana_analytics_get_campaign_cost',
        python_callable=get_campaign_cost
    )

with DAG(
    dag_id="grafana_analytics_get_single_campaign_cost",
    default_args=default_args,
    description="grafana_analytics_get_single_campaign_cost",
    schedule="10 8 * * *",
    catchup=False,
    tags=["grafana_analytics"],
):
    t3 = PythonOperator(
        task_id='grafana_analytics_get_single_campaign_cost',
        python_callable=get_single_campaign_cost
    )

with DAG(
    dag_id="grafana_analytics_ga_data",
    default_args=default_args,
    description="grafana_analytics_ga_data",
    schedule="30 8 * * *",
    catchup=False,
    tags=["grafana_analytics"],
):
    t4 = PythonOperator(
        task_id='grafana_analytics_ga_data',
        python_callable=ga_data
    )

with DAG(
    dag_id="grafana_analytics_get_suffix_category",
    default_args=default_args,
    description="grafana_analytics_get_suffix_category",
    schedule="00 9 * * *",
    catchup=False,
    tags=["grafana_analytics"],
):
    t5 = PythonOperator(
        task_id='grafana_analytics_get_suffix_category',
        python_callable=get_suffix_category
    )
