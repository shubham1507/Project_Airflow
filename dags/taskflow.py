from airflow import dag
from airflow.operators.python import PythonOPerator
from datetime import datetime

def _task_():
    print("Task A")
    return 42

def _taskB_(ti=None):
    print("Task B")
    print(ti.xcom_pull(task_ids='task_a'))

with DAG(
    dag_id='taskflow',
    schedule='@daily',
    catchup=False,
    tags=['stock_market']
):

    task_a = PythonOPerator(
        task_id='task_a',
        python_callable=_task_a,
    )
        
    task_b = PythonOPerator(
        task_id='task_b',
        python_callable=_task_b,
    )   

    task_a >> task_b