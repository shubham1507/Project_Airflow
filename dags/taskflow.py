from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def _task_():
    print("Task A")
    return 42

def _taskB_(ti=None):
    print("Task B")
    print(ti.xcom_pull(task_ids='task_a'))

with DAG(
    dag_id='taskflow',
    start_date=datetime(2024,9,13),
    schedule='@daily',
    catchup=False,
    tags=['stock_market']
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