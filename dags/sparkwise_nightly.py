"""Test version of the Sparkwise nightly scoring pipeline: four tasks in order, one optional failure."""
from datetime import datetime

from airflow.sdk import dag, task

FAIL_SCORING = False   # Change to True to watch a task fail and the downstream task stop


@dag(schedule="0 2 * * *", start_date=datetime(2025, 1, 1), catchup=False,
     default_args={"retries": 1}, tags=["sparkwise"])
def sparkwise_nightly():

    @task
    def load_subscribers():
        print("Loaded 300 current subscribers.")
        return 300

    @task
    def calculate_features(count):
        print(f"Calculated twelve features for {count} subscribers.")
        return count

    @task
    def score_subscribers(count):
        if FAIL_SCORING:
            raise RuntimeError("Scoring failed: the model file is missing.")
        print(f"Scored {count} subscribers.")
        return count

    @task
    def publish_ranked_list(count):
        print(f"Published the ranked list of {count} subscribers for the retention team.")

    publish_ranked_list(score_subscribers(calculate_features(load_subscribers())))


sparkwise_nightly()
