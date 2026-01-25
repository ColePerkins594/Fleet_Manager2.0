/**
 * Type definitions for Fleet Manager application
 */

export interface Vehicle {
  id: string
  name: string
  make: string
  model: string
  year: number
  licensePlate: string
  vin: string
  status: 'active' | 'maintenance' | 'inactive'
  mileage: number
  operatorId: string | null
}

export interface Operator {
  id: string
  firstName: string
  lastName: string
  email: string
  phone: string
  licenseNumber: string
  status: 'active' | 'inactive' | 'on-leave'
  hireDate: string
  vehicleId: string | null
}

export interface Mechanic {
  id: string
  firstName: string
  lastName: string
  email: string
  phone: string
  specialization: string
  status: 'active' | 'inactive' | 'on-leave'
  hireDate: string
  certifications: string[]
}

export type EntityType = 'vehicle' | 'operator' | 'mechanic'
