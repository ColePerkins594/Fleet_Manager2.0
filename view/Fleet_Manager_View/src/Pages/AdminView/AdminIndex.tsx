/**
 * Admin Index Page
 * Main admin dashboard showing vehicles, operators, and mechanics
 */

import { useState, useEffect } from 'react'
import { Card, CardHeader, CardContent, CardItem, CardFooter, CardGrid, SkeletonCard } from '../../components'
import type { Vehicle, Operator, Mechanic } from '../../types'
import { mockVehicles, mockOperators, mockMechanics } from '../../data/mockData'

type LoadingState = 'loading' | 'loaded' | 'error'

interface AdminState {
  vehicles: { data: Vehicle[]; state: LoadingState }
  operators: { data: Operator[]; state: LoadingState }
  mechanics: { data: Mechanic[]; state: LoadingState }
}

const AdminIndex: React.FC = () => {
  const [adminState, setAdminState] = useState<AdminState>({
    vehicles: { data: [], state: 'loading' },
    operators: { data: [], state: 'loading' },
    mechanics: { data: [], state: 'loading' },
  })

  // Simulate data loading
  useEffect(() => {
    // Load vehicles
    const vehicleTimer = setTimeout(() => {
      setAdminState((prev) => ({
        ...prev,
        vehicles: { data: mockVehicles, state: 'loaded' },
      }))
    }, 1200)

    // Load operators
    const operatorTimer = setTimeout(() => {
      setAdminState((prev) => ({
        ...prev,
        operators: { data: mockOperators, state: 'loaded' },
      }))
    }, 1500)

    // Load mechanics
    const mechanicTimer = setTimeout(() => {
      setAdminState((prev) => ({
        ...prev,
        mechanics: { data: mockMechanics, state: 'loaded' },
      }))
    }, 1300)

    return () => {
      clearTimeout(vehicleTimer)
      clearTimeout(operatorTimer)
      clearTimeout(mechanicTimer)
    }
  }, [])

  const statusBadgeColor = (status: string): string => {
    switch (status) {
      case 'active':
        return 'active'
      case 'inactive':
        return 'inactive'
      case 'maintenance':
        return 'maintenance'
      case 'on-leave':
        return 'on-leave'
      default:
        return 'active'
    }
  }

  return (
    <div className="space-y-8">
      {/* Page Header */}
      <div>
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
          Admin Dashboard
        </h1>
        <p className="text-gray-600 dark:text-gray-400 mt-2">
          Manage your fleet, operators, and mechanics
        </p>
      </div>

      {/* Vehicles Section */}
      <div>
        <div className="mb-6">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
            Vehicles
          </h2>
          <p className="text-gray-600 dark:text-gray-400 mt-1">
            {adminState.vehicles.state === 'loaded'
              ? `${adminState.vehicles.data.length} vehicles in fleet`
              : 'Loading vehicles...'}
          </p>
        </div>

        <CardGrid columns={3}>
          {adminState.vehicles.state === 'loading' ? (
            <SkeletonCard count={3} />
          ) : adminState.vehicles.data.length > 0 ? (
            adminState.vehicles.data.map((vehicle) => (
              <Card key={vehicle.id}>
                <CardHeader
                  title={vehicle.name}
                  subtitle={`${vehicle.year} ${vehicle.make} ${vehicle.model}`}
                  badge={{
                    label: vehicle.status.charAt(0).toUpperCase() + vehicle.status.slice(1),
                    color: statusBadgeColor(vehicle.status),
                  }}
                />
                <CardContent>
                  <CardItem label="License Plate" value={vehicle.licensePlate} />
                  <CardItem label="VIN" value={vehicle.vin.slice(-8)} />
                  <CardItem label="Mileage" value={`${vehicle.mileage.toLocaleString()} mi`} />
                  <CardItem
                    label="Operator"
                    value={vehicle.operatorId ? 'Assigned' : 'Unassigned'}
                  />
                </CardContent>
                <CardFooter>
                  <button className="btn-primary flex-1 text-sm">View Details</button>
                  <button className="btn-secondary flex-1 text-sm">Edit</button>
                </CardFooter>
              </Card>
            ))
          ) : (
            <div className="col-span-3 text-center py-12">
              <p className="text-gray-500 dark:text-gray-400">No vehicles found</p>
            </div>
          )}
        </CardGrid>
      </div>

      {/* Operators Section */}
      <div>
        <div className="mb-6">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
            Operators
          </h2>
          <p className="text-gray-600 dark:text-gray-400 mt-1">
            {adminState.operators.state === 'loaded'
              ? `${adminState.operators.data.length} operators on staff`
              : 'Loading operators...'}
          </p>
        </div>

        <CardGrid columns={3}>
          {adminState.operators.state === 'loading' ? (
            <SkeletonCard count={3} />
          ) : adminState.operators.data.length > 0 ? (
            adminState.operators.data.map((operator) => (
              <Card key={operator.id}>
                <CardHeader
                  title={`${operator.firstName} ${operator.lastName}`}
                  subtitle={operator.email}
                  badge={{
                    label: operator.status.charAt(0).toUpperCase() + operator.status.slice(1),
                    color: statusBadgeColor(operator.status),
                  }}
                />
                <CardContent>
                  <CardItem label="Phone" value={operator.phone} />
                  <CardItem label="License #" value={operator.licenseNumber.slice(-6)} />
                  <CardItem label="Hire Date" value={operator.hireDate} />
                  <CardItem
                    label="Vehicle"
                    value={operator.vehicleId ? 'Assigned' : 'Unassigned'}
                  />
                </CardContent>
                <CardFooter>
                  <button className="btn-primary flex-1 text-sm">View Details</button>
                  <button className="btn-secondary flex-1 text-sm">Edit</button>
                </CardFooter>
              </Card>
            ))
          ) : (
            <div className="col-span-3 text-center py-12">
              <p className="text-gray-500 dark:text-gray-400">No operators found</p>
            </div>
          )}
        </CardGrid>
      </div>

      {/* Mechanics Section */}
      <div>
        <div className="mb-6">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
            Mechanics
          </h2>
          <p className="text-gray-600 dark:text-gray-400 mt-1">
            {adminState.mechanics.state === 'loaded'
              ? `${adminState.mechanics.data.length} mechanics on staff`
              : 'Loading mechanics...'}
          </p>
        </div>

        <CardGrid columns={3}>
          {adminState.mechanics.state === 'loading' ? (
            <SkeletonCard count={3} />
          ) : adminState.mechanics.data.length > 0 ? (
            adminState.mechanics.data.map((mechanic) => (
              <Card key={mechanic.id}>
                <CardHeader
                  title={`${mechanic.firstName} ${mechanic.lastName}`}
                  subtitle={mechanic.specialization}
                  badge={{
                    label: mechanic.status.charAt(0).toUpperCase() + mechanic.status.slice(1),
                    color: statusBadgeColor(mechanic.status),
                  }}
                />
                <CardContent>
                  <CardItem label="Email" value={mechanic.email} />
                  <CardItem label="Phone" value={mechanic.phone} />
                  <CardItem label="Hire Date" value={mechanic.hireDate} />
                  <CardItem
                    label="Certifications"
                    value={mechanic.certifications.length > 0 ? `${mechanic.certifications.length} certs` : 'None'}
                  />
                </CardContent>
                <CardFooter>
                  <button className="btn-primary flex-1 text-sm">View Details</button>
                  <button className="btn-secondary flex-1 text-sm">Edit</button>
                </CardFooter>
              </Card>
            ))
          ) : (
            <div className="col-span-3 text-center py-12">
              <p className="text-gray-500 dark:text-gray-400">No mechanics found</p>
            </div>
          )}
        </CardGrid>
      </div>
    </div>
  )
}

export default AdminIndex
