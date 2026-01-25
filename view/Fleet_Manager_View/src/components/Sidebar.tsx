/**
 * Sidebar Component
 * Navigation sidebar with links to different sections
 */

import { Link, useLocation } from 'react-router-dom'

interface SidebarLink {
  label: string
  path: string
  icon?: string
}

const sidebarLinks: SidebarLink[] = [
  { label: 'Dashboard', path: '/admin', icon: '📊' },
  { label: 'Mechanics', path: '/mechanics', icon: '🔧' },
  { label: 'Operators', path: '/operators', icon: '👨‍💼' },
]

export const Sidebar: React.FC = () => {
  const location = useLocation()

  const isActive = (path: string) => location.pathname === path

  return (
    <aside className="w-64 bg-white dark:bg-dark-800 border-r border-gray-200 dark:border-dark-700 h-screen flex flex-col sticky top-0">
      {/* Logo Section */}
      <div className="p-6 border-b border-gray-200 dark:border-dark-700">
        <h1 className="text-2xl font-bold text-primary-600 dark:text-primary-400">
          Fleet Manager
        </h1>
        <p className="text-xs text-gray-600 dark:text-gray-400 mt-1">
          Admin Portal
        </p>
      </div>

      {/* Navigation Links */}
      <nav className="flex-1 px-4 py-6 space-y-2">
        {sidebarLinks.map((link) => (
          <Link
            key={link.path}
            to={link.path}
            className={`sidebar-link ${isActive(link.path) ? 'active' : ''}`}
          >
            {link.icon && <span className="text-lg">{link.icon}</span>}
            <span>{link.label}</span>
          </Link>
        ))}
      </nav>

      {/* Footer */}
      <div className="p-4 border-t border-gray-200 dark:border-dark-700 text-center">
        <p className="text-xs text-gray-600 dark:text-gray-400">
          Fleet Manager v1.0
        </p>
      </div>
    </aside>
  )
}
