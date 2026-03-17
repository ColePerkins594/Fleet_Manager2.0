from datetime import datetime
from src.helpers.db_tools.enums import drivetrain_type, vehicle_status
from src.helpers.db_tools.connection import Vehicle, get_session

class VehicleDAO:
    @staticmethod
    def fetch_vehicles(account_id: int, vin: str = None, make: str = None, model: str = None, year: int = None,
                       uptime: float = None, trim: str = None, mileage: int = None, status: str = None, drivetrain: str = None,
                       efficiency: float = None, range: float = None, license_plate: str = None, operator_id: int = None, insert_date: str = None):
        filters = {"account_id": account_id}
        if vin:
            filters["vin"] = vin
        if make:
            filters["make"] = make
        if model:
            filters["model"] = model
        if year:
            filters["year"] = year
        if trim:
            filters["trim"] = trim
        if mileage:
            filters["mileage"] = mileage
        if status:
            filters["status"] = status
        if drivetrain:
            filters["drivetrain"] = drivetrain
        if efficiency:
            filters["efficiency"] = efficiency
        if range:
            filters["range"] = range
        if uptime:
            filters["uptime"] = uptime
        if license_plate:
            filters["license_plate"] = license_plate
        if operator_id:
            filters["operator_id"] = operator_id
        if insert_date:
            filters["insert_date"] = insert_date
        session = get_session()
        if session is None:
            raise ConnectionError("Failed to establish database connection")
        try:
            qsession = session.query(Vehicle)
            for term in filters:
                currfilter = filters[term]
                attr = getattr(Vehicle, term)
                qsession = qsession.filter(attr == currfilter)
            vehicles = qsession.all()
            return vehicles
        except Exception as e:
            print(f"Error occurred while fetching vehicles: {e}")
            raise RuntimeError(f"Error occurred while fetching vehicles: {e}")
        finally:
            session.close()

    @staticmethod
    def insert_vehicle(vin: str, make: str, model: str, year: int, uptime: float, account_id: str,
                       trim: str = None, mileage: int = None, status: str = None,
                       drivetrain: str = None, efficiency: float = None, range: float = None,
                       license_plate: str = None):
        ts = datetime.now()
        session = get_session()
        if ((drivetrain and drivetrain not in [d.value for d in drivetrain_type])|(status and status not in [s.value for s in vehicle_status])):
            raise ValueError(f"Invalid argument value for drivetrain or status.")
        if session is None:
            raise ConnectionError("Failed to establish database connection")
        try:
            new_vehicle = Vehicle(vin=vin, make=make, model=model, year=year, trim=trim, uptime=uptime, account_id=account_id, mileage=mileage, status=status, drivetrain=drivetrain, efficiency=efficiency, range=range, license_plate=license_plate, insert_date=ts)
            session.add(new_vehicle)
            session.commit()
            print(f"Inserted vehicle with VIN: {vin}")
            return True
        except Exception as e:
            print(f"Error occurred while inserting vehicle: {e}")
            session.rollback()
            raise RuntimeError(f"Error occurred while inserting vehicle: {e}")
        finally:
            session.close()

    @staticmethod
    def update_vehicle(vin: str, account_id: str, make: str = None, model: str = None, year: int = None, uptime: float = None,
                       trim: str = None, mileage: int = None, status: str = None,
                       drivetrain: str = None, efficiency: float = None, range: float = None,
                       license_plate: str = None, operator_id: int = None):
        session = get_session()
        if session is None:
            raise ConnectionError("Failed to establish database connection")
        try:
            vehicle = session.query(Vehicle).filter(Vehicle.vin == vin).filter(Vehicle.account_id == account_id).first()
            if vehicle is None:
                print(f"No vehicle found with VIN: {vin}")
                raise ValueError(f"No vehicle found with VIN: {vin}")
            if make:
                vehicle.make = make
            if model:
                vehicle.model = model
            if year:
                vehicle.year = year
            if uptime:
                vehicle.uptime = uptime
            if trim:
                vehicle.trim = trim
            if mileage:
                vehicle.mileage = mileage
            if status:
                if status in [s.value for s in vehicle_status]:
                    vehicle.status = status
                else:
                    raise ValueError(f"Invalid status value: {status}")
            if (drivetrain and drivetrain in [d.value for d in drivetrain_type]):
                if drivetrain in [d.value for d in drivetrain_type]:
                    vehicle.drivetrain_type = drivetrain
                else:
                    raise ValueError(f"Invalid drivetrain value: {drivetrain}")
            if efficiency:
                vehicle.efficiency = efficiency
            if range:
                vehicle.range = range
            if license_plate:
                vehicle.license_plate = license_plate
            session.commit()
            print(f"Updated vehicle with VIN: {vin}")
            return True
        except Exception as e:
            print(f"Error occurred while updating vehicle: {e}")
            session.rollback()
            raise RuntimeError(f"Error occurred while updating vehicle: {e}")
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