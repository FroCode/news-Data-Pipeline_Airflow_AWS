# News API ETL Pipeline

## Overview

This repository contains a simple ETL (Extract, Load) pipeline for fetching top headlines from the News API and uploading the data to an AWS S3 bucket. It uses Python and Apache Airflow for orchestration.

## Files

- **`news_etl.py`**: Contains the ETL process for fetching news data and uploading it to S3.
- **`news_etl_dag.py`**: Defines the Airflow DAG for scheduling and running the ETL process.

## Prerequisites

- Python 3.7 or higher
- Apache Airflow
- `requests` library
- `pandas` library
- `boto3` library (for S3 operations)
- AWS credentials configured for `boto3`

## Setup

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/news_etl.git
    cd news_etl
    ```

2. **Install Dependencies:**

    It is recommended to use a virtual environment. Install the required Python libraries using:

    ```bash
    pip install requests pandas boto3 apache-airflow
    ```

3. **Configure Airflow:**

    - Set up Apache Airflow by following the [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html).
    - Place the `news_etl_dag.py` file in your Airflow DAGs folder (usually located at `~/airflow/dags`).

4. **Configure AWS Credentials:**

    Ensure that your AWS credentials are configured. You can set up your AWS credentials using the AWS CLI:

    ```bash
    aws configure
    ```

    Alternatively, set up environment variables:

    ```bash
    export AWS_ACCESS_KEY_ID=your_access_key_id
    export AWS_SECRET_ACCESS_KEY=your_secret_access_key
    ```

5. **Modify API Key:**

    Replace the placeholder API key in `news_etl.py` with your actual News API key:

    ```python
    api_key = 'your_news_api_key'
    ```

## Usage

1. **Running the ETL Process Manually:**

    You can run the ETL process directly using Python:

    ```bash
    python news_etl.py
    ```

2. **Scheduling with Airflow:**

    - Start the Airflow web server and scheduler:

      ```bash
      airflow webserver --port 8080
      airflow scheduler
      ```

    - Access the Airflow web interface at `http://localhost:8080`.
    - Trigger the `news_etl_dag` manually or wait for it to run according to the schedule (daily).

## S3 Bucket Configuration

- Ensure you have an S3 bucket named `reddits-data` (or adjust the bucket name in `news_etl.py` accordingly).
- The pipeline saves the news data as `news.csv` in the S3 bucket.

## Error Handling

- **API Errors:** Ensure your News API key is valid and not expired. Check for HTTP response codes in the logs for detailed error messages.
- **S3 Upload Errors:** Verify that your AWS credentials have the necessary permissions to upload files to the S3 bucket.

![Capture d'écran 2024-08-08 192422](https://github.com/user-attachments/assets/bf49797e-16ef-47f3-8f4c-57ec36e54a45)
