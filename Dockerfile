FROM apache/airflow:slim-2.10.4-python3.8
WORKDIR /opt/airflow
USER root
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender1

USER airflow
RUN pip install \
    psycopg2-binary==2.9.10 \
    apache-airflow-providers-celery==3.8.2 \
    fluent-logger==0.11.1

COPY ./project ./project
RUN if [ -f "./project/requirements.txt" ]; then pip install -r ./project/requirements.txt; fi
