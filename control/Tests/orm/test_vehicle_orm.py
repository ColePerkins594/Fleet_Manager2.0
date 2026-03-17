from pathlib import Path
from src.helpers.db_tools.enums import drivetrain_type, vehicle_status

def test_fetch_vehicles_basic():
    from src.DAO.vehicle_dao import VehicleDAO
    test_id = 1
    vehicles = VehicleDAO.fetch_vehicles(account_id=1)
    for vehicle in vehicles:
        assert vehicle.account_id == test_id

def test_insert_vehicle():
    from src.DAO.vehicle_dao import VehicleDAO
    vin = "TESTVIN1234567890"
    make = "TestMake"
    model = "TestModel"
    year = 2024
    uptime = 100.0
    account_id = 1
    trim = "TestTrim"
    mileage = 1000
    status = vehicle_status.available.value
    drivetrain = drivetrain_type.ev.value
    efficiency = 25.5
    range = 300.0
    license_plate = "TEST123"
    try:
        VehicleDAO.insert_vehicle(vin=vin, make=make, model=model, year=year, uptime=uptime, account_id=account_id,
                              trim=trim, mileage=mileage, status=status, drivetrain=drivetrain,
                              efficiency=efficiency, range=range, license_plate=license_plate)

        vehicles = VehicleDAO.fetch_vehicles(account_id=account_id, vin=vin)

        assert len(vehicles) == 1
        vehicle = vehicles[0]
        assert vehicle.vin == vin
        assert vehicle.make == make
        assert vehicle.model == model
        assert vehicle.year == year
        assert vehicle.uptime == uptime
        assert vehicle.account_id == account_id
        assert vehicle.trim == trim
        assert vehicle.mileage == mileage
        assert vehicle.status == status
        assert vehicle.drivetrain == drivetrain
        assert float(vehicle.efficiency) == efficiency
        assert vehicle.range == range
        assert vehicle.license_plate == license_plate
    except Exception as e:
        print(f"Error during test_insert_vehicle: {e}")
        assert False, f"Exception occurred: {e}"
    finally:
        from src.helpers.db_tools.connection import get_session, Vehicle
        session = get_session()
        if session:
            try:
                vehicle_to_delete = session.query(Vehicle).filter_by(vin=vin).first()
                if vehicle_to_delete:
                    session.delete(vehicle_to_delete)
                    session.commit()
            except Exception as e:
                print(f"Error during cleanup in test_insert_vehicle: {e}")
            finally:
                session.close()

def test_update_vehicle():
    from src.DAO.vehicle_dao import VehicleDAO
    vin = "TESTVIN1234567892"
    make = "TestMake"
    model = "TestModel"
    year = 2024
    uptime = 100.0
    account_id = 1
    trim = "TestTrim"
    mileage = 1000
    status = vehicle_status.available.value
    drivetrain = drivetrain_type.ev.value
    efficiency = 25.5
    range = 300.0
    license_plate = "TEST123"
    try:
        VehicleDAO.insert_vehicle(vin=vin, make=make, model=model, year=year, uptime=uptime, account_id=account_id,
                              trim=trim, mileage=mileage, status=status, drivetrain=drivetrain,
                              efficiency=efficiency, range=range, license_plate=license_plate)

        new_status = vehicle_status.out_of_service.value
        VehicleDAO.update_vehicle(vin=vin, account_id=account_id, status=new_status)
        vehicles = VehicleDAO.fetch_vehicles(account_id=account_id, vin=vin)
        assert len(vehicles) == 1
        vehicle = vehicles[0]
        assert vehicle.vin == vin
        assert vehicle.make == make
        assert vehicle.model == model
        assert vehicle.year == year
        assert vehicle.uptime == uptime
        assert vehicle.account_id == account_id
        assert vehicle.trim == trim
        assert vehicle.mileage == mileage
        assert vehicle.status == new_status
        assert vehicle.drivetrain == drivetrain
        assert float(vehicle.efficiency) == efficiency
        assert vehicle.range == range
        assert vehicle.license_plate == license_plate

    except Exception as e:
        print(f"Error during test_insert_vehicle: {e}")
        assert False, f"Exception occurred: {e}"
    finally:
        from src.helpers.db_tools.connection import get_session, Vehicle
        session = get_session()
        if session:
            try:
                vehicle_to_delete = session.query(Vehicle).filter_by(vin=vin).first()
                if vehicle_to_delete:
                    session.delete(vehicle_to_delete)
                    session.commit()
            except Exception as e:
                print(f"Error during cleanup in test_insert_vehicle: {e}")
            finally:
                session.close()

def test_delete_vehicle():
    from src.DAO.vehicle_dao import VehicleDAO
    vin = "TESTVIN1234567891"
    make = "TestMake"
    model = "TestModel"
    year = 2024
    uptime = 100.0
    account_id = 1
    trim = "TestTrim"
    mileage = 1000
    status = vehicle_status.available.value
    drivetrain = drivetrain_type.ev.value
    efficiency = 25.5
    range = 300.0
    license_plate = "TEST123"
    try:
        VehicleDAO.insert_vehicle(vin=vin, make=make, model=model, year=year, uptime=uptime, account_id=account_id,
                              trim=trim, mileage=mileage, status=status, drivetrain=drivetrain,
                              efficiency=efficiency, range=range, license_plate=license_plate)
        VehicleDAO.delete_vehicle(vin=vin)
        vehicles = VehicleDAO.fetch_vehicles(vin=vin, account_id=account_id)
        assert len(vehicles) == 0
    except Exception as e:
        print(f"Error during setup in test_delete_vehicle: {e}")
        assert False, f"Exception occurred during setup: {e}"

    