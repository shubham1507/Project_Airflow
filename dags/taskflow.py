from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def _task_a():
    print("Task A")
    return 42

def _task_b(ti=None):
    print("Task B")
    print(ti.xcom_pull(task_ids='task_a'))

with DAG(
    dag_id='taskflow',
    start_date=datetime(2024,9,13),
    schedule='@daily',
    catchup=False,
    tags=['taskflow1']
):

    task_a = PythonOperator(
        task_id='task_a',
        python_callable=_task_a,
    )
        
    task_b = PythonOperator(
        task_id='task_b',
        python_callable=_task_b,
    )   

    task_a >> task_b