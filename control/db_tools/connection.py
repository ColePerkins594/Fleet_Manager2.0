import psycopg2
import os
HOSTNAME = os.getenv("DBHOSTNAME")
USERNAME = os.getenv("DBUSERNAME")
PW = os.getenv("DBPW")
PORT = os.getenv("DBPORT")