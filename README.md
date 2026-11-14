# Sparkwise Airflow

Apache Airflow in a GitHub Codespace for the Data Engineering course.

## Start Airflow

1. On this repository's GitHub page, select **Code > Codespaces > Create codespace on main**.
2. Wait for the codespace to finish building. The first build installs Airflow and takes several minutes.
3. In the terminal, confirm that Airflow is installed:

   ```
   airflow version
   ```

4. Start Airflow:

   ```
   bash start_airflow.sh
   ```

5. Wait about a minute, until the log repeats `Not time to refresh` messages. Leave the terminal running.
6. Open the **Ports** tab (under **...** next to **Terminal**) and select the globe icon next to port **8080**.

## Stop Airflow

1. Press **Ctrl+C** in the terminal (twice if Airflow does not stop).
2. On GitHub, select **Code > Codespaces**, select **...** next to the codespace, then **Stop codespace**, so the codespace stops using free hours.
