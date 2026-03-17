import os
import sys
import os
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
    operator_id = 1

    VehicleDAO.insert_vehicle(vin=vin, make=make, model=model, year=year, uptime=uptime, account_id=account_id,
                              trim=trim, mileage=mileage, status=status, drivetrain=drivetrain,
                              efficiency=efficiency, range=range, license_plate=license_plate,
                              operator_id=operator_id)

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
    assert vehicle.efficiency == efficiency
    assert vehicle.range == range
    assert vehicle.license_plate == license_plate
    assert vehicle.operator_id == operator_id