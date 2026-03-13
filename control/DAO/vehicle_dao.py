import os
import sys
import os
from pathlib import Path

my_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.insert(0, str(my_path))
from db_tools.connection import Vehicle, get_session

class VehicleDAO:
    @staticmethod
    def fetch_vehicles(account_id: int, vin: str = None, make: str = None, model: str = None, year: int = None, trim: str = None, mileage: int = None, status: str = None, drivetrain: str = None, efficiency: float = None, range: float = None, license_plate: str = None, operator_id: int = None, insert_date: str = None):
        session = get_session()
        if session is None:
            return []
        try:
            vehicles = session.query(Vehicle).filter(Vehicle.make == "Toyota").all()
            for vehicle in vehicles:
                print(f"Vehicle ID: {vehicle.vin}, Make: {vehicle.make}, Model: {vehicle.model}, Year: {vehicle.year}")
            return vehicles
        except Exception as e:
            print(f"Error occurred while fetching vehicles: {e}")
            return []
        finally:
            session.close()

    @staticmethod
    def insert_vehicle(vin: str, make: str, model: str, year: int):
        session = get_session()
        if session is None:
            return False
        try:
            new_vehicle = Vehicle(vin=vin, make=make, model=model, year=year)
            session.add(new_vehicle)
            session.commit()
            print(f"Inserted vehicle with VIN: {vin}")
            return True
        except Exception as e:
            print(f"Error occurred while inserting vehicle: {e}")
            session.rollback()
            return False
        finally:
            session.close()

    @staticmethod
    def update_vehicle(vin: str, make: str = None, model: str = None, year: int = None):
        session = get_session()
        if session is None:
            return False
        try:
            vehicle = session.query(Vehicle).filter(Vehicle.vin == vin).first()
            if vehicle is None:
                print(f"No vehicle found with VIN: {vin}")
                return False
            if make is not None:
                vehicle.make = make
            if model is not None:
                vehicle.model = model
            if year is not None:
                vehicle.year = year
            session.commit()
            print(f"Updated vehicle with VIN: {vin}")
            return True
        except Exception as e:
            print(f"Error occurred while updating vehicle: {e}")
            session.rollback()
            return False
        finally:
            session.close()

    @staticmethod
    def delete_vehicle(vin: str):
        session = get_session()
        if session is None:
            return False
        try:
            vehicle = session.query(Vehicle).filter(Vehicle.vin == vin).first()
            if vehicle is None:
                print(f"No vehicle found with VIN: {vin}")
                return False
            session.delete(vehicle)
            session.commit()
            print(f"Deleted vehicle with VIN: {vin}")
            return True
        except Exception as e:
            print(f"Error occurred while deleting vehicle: {e}")
            session.rollback()
            return False
        finally:
            session.close()