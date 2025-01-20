FROM apache/airflow:slim-2.10.4-python3.8
USER airflow
RUN pip install psycopg2-binary==2.9.10 apache-airflow-providers-celery==3.8.2
