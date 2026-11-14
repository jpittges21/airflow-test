"""Sparkwise nightly pipeline: score current subscribers and send the retention team a ranked list."""
from datetime import datetime, timedelta

from airflow.sdk import dag, task

QUALITY_CHECK_FAILS = False   # Change to True to make check_quality fail


@dag(
    schedule="0 2 * * *",                      # 2:00 a.m. every day
    start_date=datetime(2025, 1, 1),
    catchup=False,                             # do not run missed past dates
    default_args={"retries": 2,                # two more attempts after a failure
                  "retry_delay": timedelta(minutes=1)},
    tags=["sparkwise"],
)
def sparkwise_nightly():

    @task
    def extract_activity():
        print("Extracted 1,214 activity records from the activity database.")
        return "activity.csv"

    @task
    def check_quality(activity_file):
        if QUALITY_CHECK_FAILS:
            raise ValueError("Quality check failed: 38% of activity records have no subscriber ID.")
        print(f"Quality check passed for {activity_file}.")
        return activity_file

    @task
    def calculate_features(activity_file):
        print(f"Calculated subscriber features from {activity_file}.")
        return "features.csv"

    @task
    def score_subscribers(feature_table):
        print(f"Scored 300 subscribers from {feature_table}.")
        return "probabilities.csv"

    @task
    def publish_list(probabilities):
        print(f"Published the ranked list from {probabilities}, replacing the previous list.")
        return "ranked_list.csv"

    @task
    def notify_team(ranked_list):
        print(f"Notified the retention team: {ranked_list} is ready.")

    activity = extract_activity()
    checked = check_quality(activity)
    features = calculate_features(checked)
    notify_team(publish_list(score_subscribers(features)))


sparkwise_nightly()
