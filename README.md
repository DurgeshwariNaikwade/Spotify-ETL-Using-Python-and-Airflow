# Spotify-ETL-Using-Python-and-Airflow

# ****Building Spotify ETL using Python and Airflow****

![spotify_etl](https://github.com/DurgeshwariNaikwade/Spotify-ETL-Using-Python-and-Airflow/assets/96798708/b7eef748-364b-437d-bff1-067f4a96f6dc)

## **Introduction**

The Spotify ETL (Extract, Transform, Load) project aims to retrieve user-specific song data from the Spotify API, perform data transformations, and load the transformed data into a PostgreSQL database. The project utilizes Python and Apache Airflow, an open-source platform for workflow automation.

## **Prerequisites**

Before starting the project, ensure the following:

1. Log in to Spotify Developer website and create an app to obtain the client ID and secret code.
2. Set up the Spotify API with the appropriate URI for the desired API endpoint.
3. Install the required Python libraries: requests, spotipy, pandas, sqlalchemy.
4. Set up Docker and Docker Compose to run Airflow in a containerized environment.
5. Create a PostgreSQL database for storing the extracted and transformed data.

## **Running the ETL Pipeline**

To run the ETL pipeline, follow these steps:

1. Log in to the Spotify Developer website and create an app. Obtain the client ID and secret code.
2. Install the required Python libraries by running **`pip install requests spotipy pandas sqlalchemy`**.
3. Set up Docker and Docker Compose.
4. Create a PostgreSQL database and update the connection details in the code.
5. Start Airflow using Docker Compose by running **`docker-compose up -d`**.
6. Access the Airflow UI by visiting **`http://localhost:8080`** in your web browser.
7. Configure the PostgreSQL connection in Airflow using the Airflow UI.
8. Place the necessary files (**`spotify_etl.py`**, **`spotify_final_dag.py`**) in the appropriate directories (**`dags/`** ).
9. Enable the **`spotify_final_dag`** in the Airflow UI.
10. Trigger the DAG manually or set up a schedule to run the pipeline automatically.

## **Project Steps**

### **1. Getting Spotify API Access Token Using Python**

To access user-specific song data from the Spotify API, an access token is required. The project provides Python code to obtain the access token by following the steps below:

- Logging into Spotify
- Creating a Spotify developer app and obtaining the Client ID and Secret Code
- Using the Spotipy library to authenticate and obtain the access token

### **2. Data Extraction and Transformation**

The project includes Python code to extract song data from the Spotify API. This involves:

- Retrieving recently played songs for a user within a specified time frame
- Parsing the JSON response and extracting relevant information such as song name, artist name, played timestamp, and more
- Performing data quality checks to ensure data integrity and validity
- refer: get_token.py
    

### **3. Data Loading into PostgreSQL Database**

Once the data is extracted and transformed, it is loaded into a PostgreSQL database. The project includes code to create the necessary table and load the data into the table using the psycopg2 library. Data quality checks are performed before loading to ensure data consistency.

- Refer: Spotify_etl.py(Contains Python code to extract data from the Spotify API, transform it, and return a pandas DataFrame.)
- Refer: spotify_final_dag.py (Defines the Airflow DAG (Directed Acyclic Graph) for orchestrating the ETL pipeline.)

### **4. Airflow Integration**

The project incorporates Apache Airflow, a workflow management platform, to automate the ETL process. The ETL steps are converted into Airflow tasks and organized into a Directed Acyclic Graph (DAG). The DAG is scheduled to run periodically, fetching new song data and updating the database.

### **5. Docker Setup for Airflow and PostgreSQL**

The project provides instructions on setting up Airflow and PostgreSQL using Docker. Docker allows for easy containerization and deployment of the Airflow environment, including the necessary dependencies and database.

## **Monitoring and Troubleshooting**

During the execution of the ETL pipeline, you can monitor the progress and logs through the Airflow UI. Any issues or errors encountered during the pipeline execution will be logged in the Airflow logs. Additionally, you can access the PostgreSQL database to inspect the stored data and verify its correctness.

## **Conclusion**

The Spotify ETL project demonstrates the end-to-end process of extracting song data from the Spotify API, transforming it, and loading it into a PostgreSQL database. The integration of Apache Airflow automates the process, ensuring that the data is regularly updated. This project provides a foundation for further analysis and insights on user-specific Spotify streaming history

References:

[Medium(Building Spotify ETL using Python & Airflow)](https://medium.com/dev-genius/data-engineering-project-2-building-spotify-etl-using-python-and-airflow-432dd8e4ffa3)

[YouTube(Getting Spotify Access token using Python)](https://www.youtube.com/watch?v=WAmEZBEeNmg&t=953s)

[Article(Used for getting token-used in this project)](https://towardsdatascience.com/get-your-spotify-streaming-history-with-python-d5a208bbcbd3#:~:text=Getting%20the%20data,option%20to%20request%20your%20data.)

https://deepnote.com/@deepnote/Spotify-API-Exploration-f3efc11d-57f5-4908-b74e-fd4961a33a22

https://github.com/YashviP/spotify-airflow/blob/main/dags/spotify_etl.py

https://airflow.apache.org/docs/apache-airflow/stable/installation/index.html#using-production-docker-images
