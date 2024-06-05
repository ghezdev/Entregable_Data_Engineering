FROM python:3.9

RUN pip install apache-airflow[providers-postgres]

WORKDIR /opt/airflow/dags

COPY ./dags/etl.py .

COPY ./dags/entregable_dag.py .

ENV AIRFLOW_HOME /opt/airflow

EXPOSE 8080

CMD ["airflow", "scheduler"]

CMD ["airflow", "webserver"]

RUN pip install requests
RUN pip install pandas
RUN pip install psycopg2-binary