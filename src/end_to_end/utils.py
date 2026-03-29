import os
import sys
from src.end_to_end.exception import EndToEndException
from src.end_to_end.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_data_from_mysql():
    logging.info("Reading data from mysql database..........")
    try:
        mydb = pymysql.connect(host=host, user=user, password=password, db=db)
        logging.info("connection established: %s", mydb)
        df = pd.read_sql_query("SELECT * FROM students", mydb)
        logging.info("Data read successfully from mysql database.............")
        return df
    except Exception as e:
        raise EndToEndException(e, sys) from e
