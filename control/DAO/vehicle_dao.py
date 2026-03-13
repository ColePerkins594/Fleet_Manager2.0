from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from db_tools.connection import Vehicle, get_session


def get_all_vehicles():
    session = get_session()
    if session is None:
        return []
    try:
        vehicles = session.query(Vehicle).all()
        for vehicle in vehicles:
            print(f"Vehicle ID: {vehicle.VIN}, Make: {vehicle.make}, Model: {vehicle.model}, Year: {vehicle.year}")
        return vehicles
    except Exception as e:
        print(f"Error occurred while fetching vehicles: {e}")
        return []
    finally:
        session.close()

def main():
    get_all_vehicles()
main()