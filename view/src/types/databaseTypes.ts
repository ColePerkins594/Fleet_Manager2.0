// TypeScript types based on SQL schema

// ENUM types
export type UserRole = 'ADMIN' | 'OPERATOR' | 'MECHANIC';
export type UserStatus = 'ACTIVE' | 'INACTIVE' | 'ON LEAVE';
export type VehicleStatus = 'OUT OF SERVICE' | 'ON A JOB' | 'AVAILABLE';
export type Channel = 'EMAIL' | 'PHONE-SMS' | 'PHONE-VOICE';
export type DrivetrainType = 'ICE' | 'EV' | 'HYBRID' | 'PHEV';
export type ServiceType = 'MAINTENANCE' | 'REPAIR' | 'DIAGNOSIS';

// Composite type
export interface UserAddress {
    city: string;
    state: string;
    street: string;
    zip: string;
    number: string;
}

// Table types
export interface ContactPoint {
    contact_point_id: number;
    channel: Channel;
    point: string;
    is_preffered: boolean;
    user_id: number;
}

export interface Vehicle {
    vin: string;
    make: string;
    model: string;
    year: number;
    trim?: string;
    milage?: number;
    drivetrain: DrivetrainType;
    efficiency?: string;
    range?: number;
    license_plate: string;
    status: VehicleStatus;
    insert_date: Date;
    account_id: number;
}

export interface ServiceRecord {
    service_record_id: number;
    service_type: ServiceType;
    description: string;
    service_date: Date;
    completed_time?: Date;
    vehicle_id: string;
    mechanic_id: number;
}

export interface Issue {
    issue_id: number;
    description: string;
    symptoms: string;
    solution?: string;
    reported_time: Date;
    resolved_time?: Date;
    service_record_id: number;
    vehicle_id: string;
}

export interface Job {
    job_id: number;
    description: string;
    start_time: Date;
    end_time: Date;
    vehicle_id: string;
    operator_id: number;
}

export interface OperatorVehicle {
    id: number;
    assign_date: Date;
    vehicle_id: string;
}