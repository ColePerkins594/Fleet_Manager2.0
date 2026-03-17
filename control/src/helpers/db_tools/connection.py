from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import os
HOSTNAME = os.getenv("DBHOSTNAME")
USERNAME = os.getenv("DBUSERNAME")
PW = os.getenv("DBPW")
PORT = int(os.getenv("DBPORT"))
DBNAME = os.getenv("DBNAME")
Base = automap_base()
engine = create_engine(f'postgresql+psycopg2://{USERNAME}:{PW}@{HOSTNAME}:{PORT}/{DBNAME}')
Base.prepare(autoload_with=engine)

# Access the table
User = Base.classes.user
Vehicle = Base.classes.vehicle
Account = Base.classes.account
Issue = Base.classes.issue
Job = Base.classes.job
Service_Record = Base.classes.service_record
Contact_Point = Base.classes.contact_point
Operator_Vehicle = Base.classes.operator_vehicle


def get_session():
    try:
        session = Session(engine)
        return session
    except Exception as e:
        print(f"Error occurred while creating session: {e}")
        return None