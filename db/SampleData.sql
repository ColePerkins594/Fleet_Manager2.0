-- Sample Data for Fleet Manager Database
-- This script inserts test data into all tables, with all records related to an account

-- Insert 1 account
INSERT INTO account (name) VALUES ('ABC Transport Company');

-- Insert 10+ users (various roles) related to the account
INSERT INTO "user" (first_name, last_name, role, status, age, addr, account_id) VALUES
('John', 'Smith', 'ADMIN', 'ACTIVE', 45, ROW('Denver', 'CO', '123 Main St', '80202', '100'), 1),
('Sarah', 'Johnson', 'OPERATOR', 'ACTIVE', 32, ROW('Denver', 'CO', '456 Oak Ave', '80203', '200'), 1),
('Michael', 'Williams', 'OPERATOR', 'ACTIVE', 28, ROW('Denver', 'CO', '789 Pine Rd', '80204', '300'), 1),
('Jessica', 'Brown', 'MECHANIC', 'ACTIVE', 38, ROW('Denver', 'CO', '321 Elm St', '80205', '400'), 1),
('David', 'Davis', 'MECHANIC', 'ACTIVE', 42, ROW('Denver', 'CO', '654 Maple Dr', '80206', '500'), 1),
('Emily', 'Miller', 'OPERATOR', 'ACTIVE', 26, ROW('Denver', 'CO', '987 Birch Ln', '80207', '600'), 1),
('Robert', 'Wilson', 'ADMIN', 'ACTIVE', 50, ROW('Denver', 'CO', '147 Cedar Way', '80208', '700'), 1),
('Amanda', 'Moore', 'OPERATOR', 'ON LEAVE', 31, ROW('Denver', 'CO', '258 Spruce St', '80209', '800'), 1),
('Thomas', 'Taylor', 'MECHANIC', 'ACTIVE', 35, ROW('Denver', 'CO', '369 Walnut Dr', '80210', '900'), 1),
('Jennifer', 'Anderson', 'OPERATOR', 'INACTIVE', 29, ROW('Denver', 'CO', '741 Sycamore Rd', '80211', '1000'), 1),
('Christopher', 'Thomas', 'MECHANIC', 'ACTIVE', 40, ROW('Denver', 'CO', '852 Ash Ave', '80212', '1100'), 1),
('Linda', 'Jackson', 'OPERATOR', 'ACTIVE', 27, ROW('Denver', 'CO', '963 Oak St', '80213', '1200'), 1);

-- Insert 10+ contact points for users
INSERT INTO contact_point (channel, point, is_preffered, user_id) VALUES
('EMAIL', 'john.smith@company.com', true, 1),
('PHONE-VOICE', '303-555-0101', false, 1),
('EMAIL', 'sarah.johnson@company.com', true, 2),
('PHONE-SMS', '303-555-0102', true, 2),
('EMAIL', 'michael.williams@company.com', true, 3),
('PHONE-VOICE', '303-555-0103', false, 3),
('EMAIL', 'jessica.brown@company.com', true, 4),
('PHONE-SMS', '303-555-0104', true, 4),
('EMAIL', 'david.davis@company.com', true, 5),
('PHONE-VOICE', '303-555-0105', false, 5),
('EMAIL', 'emily.miller@company.com', true, 6),
('PHONE-SMS', '303-555-0106', true, 6),
('EMAIL', 'robert.wilson@company.com', true, 7),
('PHONE-VOICE', '303-555-0107', true, 7),
('EMAIL', 'amanda.moore@company.com', false, 8),
('PHONE-SMS', '303-555-0108', true, 8);

-- Insert 10+ vehicles related to the account
INSERT INTO vehicle (vin, make, model, year, trim, milage, drivetrain, efficiency, range, license_plate, uptime, status, insert_date, account_id) VALUES
('1HGCV41JXMN109186', 'Honda', 'Civic', 2022, 'EX', 15000, 'ICE', '28 mpg', NULL, 'ABC-001', 98.5, 'AVAILABLE', '2024-01-15 08:00:00', 1),
('2HGCV41JXMN109187', 'Toyota', 'Camry', 2021, 'LE', 28000, 'HYBRID', '52 mpg', NULL, 'ABC-002', 97.2, 'ON A JOB', '2024-02-20 09:30:00', 1),
('3HGCV41JXMN109188', 'Ford', 'Transit', 2023, 'Standard', 5000, 'ICE', '18 mpg', NULL, 'ABC-003', 99.1, 'AVAILABLE', '2024-03-10 07:15:00', 1),
('4HGCV41JXMN109189', 'Tesla', 'Model 3', 2022, 'Long Range', 12000, 'EV', NULL, 315, 'ABC-004', 96.8, 'AVAILABLE', '2024-01-22 10:45:00', 1),
('5HGCV41JXMN109190', 'Nissan', 'Altima', 2020, 'SV', 45000, 'ICE', '32 mpg', NULL, 'ABC-005', 95.3, 'ON A JOB', '2024-02-05 08:20:00', 1),
('6HGCV41JXMN109191', 'Chevrolet', 'Silverado', 2022, 'LT', 22000, 'ICE', '22 mpg', NULL, 'ABC-006', 98.0, 'OUT OF SERVICE', '2024-01-30 06:00:00', 1),
('7HGCV41JXMN109192', 'Hyundai', 'Ioniq', 2023, 'Hybrid', 8000, 'HYBRID', '58 mpg', NULL, 'ABC-007', 99.5, 'AVAILABLE', '2024-03-01 09:00:00', 1),
('8HGCV41JXMN109193', 'BMW', 'i4', 2023, 'eDrive40', 6000, 'EV', NULL, 260, 'ABC-008', 98.9, 'ON A JOB', '2024-02-28 07:30:00', 1),
('9HGCV41JXMN109194', 'Mercedes', 'E-Class', 2021, 'E350', 35000, 'ICE', '25 mpg', NULL, 'ABC-009', 96.5, 'AVAILABLE', '2024-01-10 08:45:00', 1),
('AHGCV41JXMN109195', 'Volvo', 'XC90', 2022, 'T6 Inscription', 18000, 'PHEV', '45 mpg', 280, 'ABC-010', 97.8, 'ON A JOB', '2024-02-15 07:00:00', 1),
('BHGCV41JXMN109196', 'Mazda', 'CX-5', 2020, 'Premium', 52000, 'ICE', '28 mpg', NULL, 'ABC-011', 94.2, 'AVAILABLE', '2024-01-05 10:15:00', 1),
('CHGCV41JXMN109197', 'Volkswagen', 'ID.4', 2023, 'Standard', 4000, 'EV', NULL, 275, 'ABC-012', 99.7, 'AVAILABLE', '2024-03-05 08:30:00', 1);

-- Insert 10+ service records for the vehicles and mechanics
INSERT INTO service_record (service_type, description, service_date, completed_time, vehicle_id, mechanic_id) VALUES
('MAINTENANCE', 'Oil change and filter replacement', '2024-01-20 09:00:00', '2024-01-20 10:30:00', '1HGCV41JXMN109186', 4),
('MAINTENANCE', 'Tire rotation and alignment check', '2024-02-01 08:30:00', '2024-02-01 11:00:00', '2HGCV41JXMN109187', 5),
('REPAIR', 'Battery replacement', '2024-02-10 10:00:00', '2024-02-10 14:00:00', '4HGCV41JXMN109189', 9),
('DIAGNOSIS', 'Engine light diagnostic scan', '2024-02-15 07:30:00', '2024-02-15 08:45:00', '5HGCV41JXMN109190', 4),
('MAINTENANCE', 'Fluid top-up and inspection', '2024-02-20 09:00:00', '2024-02-20 09:45:00', '3HGCV41JXMN109188', 11),
('REPAIR', 'Brake pad replacement', '2024-02-25 08:00:00', '2024-02-25 12:30:00', '6HGCV41JXMN109191', 5),
('MAINTENANCE', 'Air filter and cabin filter replacement', '2024-03-01 10:00:00', '2024-03-01 11:15:00', '7HGCV41JXMN109192', 9),
('DIAGNOSIS', 'Transmission fluid diagnostic', '2024-03-05 07:00:00', '2024-03-05 08:20:00', '8HGCV41JXMN109193', 4),
('REPAIR', 'Suspension repair and alignment', '2024-03-10 09:30:00', '2024-03-10 16:00:00', '9HGCV41JXMN109194', 11),
('MAINTENANCE', 'Coolant flush and refill', '2024-03-12 08:00:00', '2024-03-12 09:30:00', 'AHGCV41JXMN109195', 5),
('REPAIR', 'Windshield replacement', '2024-03-15 08:30:00', '2024-03-15 10:00:00', 'BHGCV41JXMN109196', 9),
('DIAGNOSIS', 'Electrical system check', '2024-03-18 10:00:00', '2024-03-18 11:45:00', 'CHGCV41JXMN109197', 4);

-- Insert 10+ issues related to vehicles and service records
INSERT INTO issue (description, symptoms, solution, reported_time, resolved_time, service_record_id, vehicle_id) VALUES
('Engine knock detected', 'Knocking sound from engine during acceleration', 'Adjusted fuel quality, replaced spark plugs', '2024-02-15 07:15:00', '2024-02-15 08:45:00', 4, '5HGCV41JXMN109190'),
('Battery low charge', 'Vehicle not starting, battery warning light', 'Battery tested and replaced', '2024-02-10 09:30:00', '2024-02-10 14:00:00', 3, '4HGCV41JXMN109189'),
('Oil leak detected', 'Oil puddle under vehicle, low oil level warning', 'Oil drain pan sealed, new oil added', '2024-01-20 08:45:00', '2024-01-20 10:30:00', 1, '1HGCV41JXMN109186'),
('Tire uneven wear', 'Front tires wearing faster on inner edge', 'Wheel alignment performed, tires rotated', '2024-02-01 08:00:00', '2024-02-01 11:00:00', 2, '2HGCV41JXMN109187'),
('Brake squeaking', 'Squeaking noise when braking', 'Brake pads inspected and replaced', '2024-02-25 07:45:00', '2024-02-25 12:30:00', 6, '6HGCV41JXMN109191'),
('Air filter clogged', 'Reduced engine performance, check engine light', 'Air filter replaced', '2024-03-01 09:30:00', '2024-03-01 11:15:00', 7, '7HGCV41JXMN109192'),
('Transmission slipping', 'Engine revs high without acceleration', 'Transmission fluid flushed and replaced', '2024-03-05 06:45:00', '2024-03-05 08:20:00', 8, '8HGCV41JXMN109193'),
('Suspension noise', 'Clunking sound over bumps', 'Suspension components tightened and lubricated', '2024-03-10 09:00:00', '2024-03-10 16:00:00', 9, '9HGCV41JXMN109194'),
('Coolant leak', 'Engine overheating, coolant level low', 'Coolant system flushed, leak sealed', '2024-03-12 07:45:00', '2024-03-12 09:30:00', 10, 'AHGCV41JXMN109195'),
('Windshield crack', 'Large crack across windshield affecting visibility', 'Windshield replaced with OEM glass', '2024-03-15 08:00:00', '2024-03-15 10:00:00', 11, 'BHGCV41JXMN109196'),
('Electrical fault', 'Dashboard lights flickering, battery not charging', 'Alternator tested and replaced', '2024-03-18 09:30:00', '2024-03-18 11:45:00', 12, 'CHGCV41JXMN109197'),
('Check engine light', 'Engine light illuminated, vehicle runs rough', 'Oxygen sensor replaced', '2024-02-20 08:15:00', NULL, 5, '3HGCV41JXMN109188');

-- Insert 10+ jobs for operators with vehicles
INSERT INTO job (description, start_time, end_time, vehicle_id, operator_id) VALUES
('Delivery to Downtown Denver', '2024-02-01 08:00:00', '2024-02-01 12:30:00', '2HGCV41JXMN109187', 2),
('Transport supplies to warehouse', '2024-02-05 07:30:00', '2024-02-05 16:00:00', '5HGCV41JXMN109190', 3),
('Client meeting transport', '2024-02-10 09:00:00', '2024-02-10 14:00:00', '8HGCV41JXMN109193', 6),
('Weekly supply run', '2024-02-15 08:00:00', '2024-02-15 17:00:00', '1HGCV41JXMN109186', 2),
('Equipment delivery', '2024-02-20 06:00:00', '2024-02-20 18:00:00', '10HGCV41JXMN109195', 12),
('Service appointment transport', '2024-02-25 10:00:00', '2024-02-25 15:30:00', '4HGCV41JXMN109189', 3),
('Executive transport', '2024-03-01 07:00:00', '2024-03-01 17:00:00', '9HGCV41JXMN109194', 6),
('Package delivery route', '2024-03-05 08:30:00', '2024-03-05 18:00:00', 'BHGCV41JXMN109196', 2),
('Long distance freight haul', '2024-03-10 05:00:00', '2024-03-10 22:00:00', '7HGCV41JXMN109192', 12),
('Emergency response transport', '2024-03-15 14:30:00', '2024-03-15 16:45:00', 'CHGCV41JXMN109197', 3),
('Client site visit', '2024-03-18 09:00:00', NULL, '2HGCV41JXMN109187', 6);

-- Insert 10+ operator vehicle assignments
INSERT INTO operator_vehicle (assign_date, vehicle_id, operator_id) VALUES
('2024-01-15 08:00:00', '1HGCV41JXMN109186', 2),
('2024-01-15 08:00:00', '2HGCV41JXMN109187', 3),
('2024-01-15 08:00:00', '3HGCV41JXMN109188', 6),
('2024-01-15 08:00:00', '4HGCV41JXMN109189', 12),
('2024-01-20 09:00:00', '5HGCV41JXMN109190', 2),
('2024-01-20 09:00:00', '6HGCV41JXMN109191', 3),
('2024-02-01 10:00:00', '7HGCV41JXMN109192', 6),
('2024-02-01 10:00:00', '8HGCV41JXMN109193', 12),
('2024-02-10 08:00:00', '9HGCV41JXMN109194', 2),
('2024-02-10 08:00:00', 'AHGCV41JXMN109195', 3),
('2024-02-15 09:00:00', 'BHGCV41JXMN109196', 6),
('2024-03-01 10:00:00', 'CHGCV41JXMN109197', 12);
