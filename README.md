# Airflow Test

Test of Apache Airflow in GitHub Codespaces for the Data Engineering course.

## Steps

1. On this repository's GitHub page, select **Code > Codespaces > Create codespace on main**.
2. Wait for the codespace to finish building. The first build installs Airflow (several minutes).
   The terminal ends with the Airflow version number.
3. In the terminal, run:

   ```
   airflow standalone
   ```

4. Wait for the line `Airflow is ready`. A notice offers to open port 8080; select **Open in Browser**.
   (Or open the **Ports** tab and select the globe icon next to port 8080.)
5. If Airflow asks for a login, the user is `admin` and the password is in
   `.airflow/simple_auth_manager_passwords.json.generated`.
6. In the Airflow web page, open **hello_airflow** and select **Trigger**. The task turns green.
7. Open **sparkwise_nightly**, trigger the DAG, and open the **Graph** view: four tasks run in order.
8. Optional failure test: in `dags/sparkwise_nightly.py`, set `FAIL_SCORING = True`, save, wait about
   30 seconds, and trigger again. `score_subscribers` retries once, then fails, and
   `publish_ranked_list` does not run.
9. When finished, stop Airflow with Ctrl+C, then stop the codespace (**Code > Codespaces > ... > Stop**)
   so the codespace stops using free hours.

## Report

For each step, note whether the step worked and copy any error message.
