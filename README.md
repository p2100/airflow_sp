# airflow_sp
Airflow运行的sp后台任务

- .env
```angular2html
AIRFLOW_UID=50000
AIRFLOW__CORE__FERNET_KEY=''

AIRFLOW__CELERY__RESULT_BACKEND='db+postgresql://'
AIRFLOW__CELERY__BROKER_URL=''
AIRFLOW__DATABASE__SQL_ALCHEMY_CONN='postgresql+psycopg2://'

_AIRFLOW_WWW_USER_USERNAME=''
_AIRFLOW_WWW_USER_PASSWORD=''
```

- _AIRFLOW_WWW_USER_USERNAME:
  init时设置初始用户，但是在用户表已存在初始用户时不会**重新创建或更新**
