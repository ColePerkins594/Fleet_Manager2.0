/**
 * Layout Component
 * Main layout wrapper with sidebar and content area
 */

import { Outlet } from 'react-router-dom'
import { Sidebar } from './Sidebar'

export const Layout: React.FC = () => {
  return (
    <div className="flex h-screen w-full bg-gray-50 dark:bg-dark-900">
      {/* Sidebar */}
      <Sidebar />

      {/* Main Content Area */}
      <main className="flex-1 overflow-auto">
        <div className="p-8">
          <Outlet />
        </div>
      </main>
    </div>
  )
}
