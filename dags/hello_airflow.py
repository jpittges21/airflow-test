"""Smallest possible DAG: confirms that Airflow finds and runs DAG files."""
from datetime import datetime

from airflow.sdk import dag, task


@dag(schedule=None, start_date=datetime(2025, 1, 1), catchup=False, tags=["test"])
def hello_airflow():

    @task
    def say_hello():
        print("Airflow is running.")

    say_hello()


hello_airflow()
