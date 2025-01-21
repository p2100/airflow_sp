FROM apache/airflow:slim-2.10.4-python3.8
WORKDIR /opt/airflow
USER airflow
RUN pip install psycopg2-binary==2.9.10 apache-airflow-providers-celery==3.8.2
RUN if [ ! -f "./project/requirements.txt" ]; then \\
    touch "./project/requirements.txt"; \\
    fi \
COPY ./project/requirements.txt /opt/airflow/project/requirements.txt
RUN pip install -r ./project/requirements.txt
