/**
 * Router configuration
 * Centralized router setup using createBrowserRouter (React Router v6)
 */

import { createBrowserRouter, Navigate } from 'react-router-dom'
import { Layout } from './components'
import AdminIndex from './Pages/AdminView/AdminIndex'

export const router = createBrowserRouter([
  {
    path: '/',
    element: <Layout />,
    children: [
      {
        index: true,
        element: <Navigate to="/admin" replace />,
      },
      {
        path: 'admin',
        element: <AdminIndex />,
      },
      {
        path: 'mechanics',
        element: (
          <div className="text-center py-12">
            <p className="text-gray-600 dark:text-gray-400">
              Mechanics page coming soon...
            </p>
          </div>
        ),
      },
      {
        path: 'operators',
        element: (
          <div className="text-center py-12">
            <p className="text-gray-600 dark:text-gray-400">
              Operators page coming soon...
            </p>
          </div>
        ),
      },
    ],
  },
])
