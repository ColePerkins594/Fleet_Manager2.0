from enum import Enum

class user_role(Enum):
    admin = "ADMIN"
    operator = "OPERATOR"
    mechanic = "MECHANIC"

class user_status(Enum):
    active = "ACTIVE"
    inactive = "INACTIVE"
    suspended = "ON LEAVE"

class vehicle_status(Enum):
    available = "AVAILABLE"
    on_job = "ON A JOB"
    out_of_service = "OUT OF SERVICE"

class channel(Enum):
    email = "EMAIL"
    sms = "PHONE-SMS"
    phone = "PHONE-VOICE"

class drivetrain_type(Enum):
    ice = "ICE"
    ev = "EV"
    hybrid = "HYBRID"
    phev = "PHEV"

class service_type(Enum):
    maintenance = "MAINTENANCE"
    repair = "REPAIR"
    inspection = "DIAGNOSIS"
