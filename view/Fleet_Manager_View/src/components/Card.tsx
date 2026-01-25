/**
 * Card Component
 * Generic card component for displaying content
 */

import React from 'react'

interface CardProps {
  children: React.ReactNode
  className?: string
  onClick?: () => void
}

export const Card: React.FC<CardProps> = ({ children, className = '', onClick }) => {
  return (
    <div
      className={`card p-6 cursor-pointer ${onClick ? 'hover:shadow-xl' : ''} ${className}`}
      onClick={onClick}
      role={onClick ? 'button' : undefined}
      tabIndex={onClick ? 0 : undefined}
      onKeyDown={onClick ? (e) => e.key === 'Enter' && onClick() : undefined}
    >
      {children}
    </div>
  )
}

interface CardHeaderProps {
  title: string
  subtitle?: string
  badge?: { label: string; color: string }
}

export const CardHeader: React.FC<CardHeaderProps> = ({ title, subtitle, badge }) => {
  const statusColors: Record<string, string> = {
    active: 'bg-green-100 dark:bg-green-900 text-green-800 dark:text-green-200',
    inactive: 'bg-red-100 dark:bg-red-900 text-red-800 dark:text-red-200',
    maintenance: 'bg-yellow-100 dark:bg-yellow-900 text-yellow-800 dark:text-yellow-200',
    'on-leave': 'bg-blue-100 dark:bg-blue-900 text-blue-800 dark:text-blue-200',
  }

  return (
    <div className="flex items-start justify-between gap-4">
      <div className="flex-1">
        <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
          {title}
        </h3>
        {subtitle && (
          <p className="text-sm text-gray-600 dark:text-gray-400 mt-1">
            {subtitle}
          </p>
        )}
      </div>
      {badge && (
        <span
          className={`inline-flex items-center px-3 py-1 rounded-full text-xs font-medium whitespace-nowrap ${
            statusColors[badge.color] || statusColors.active
          }`}
        >
          {badge.label}
        </span>
      )}
    </div>
  )
}

interface CardContentProps {
  children: React.ReactNode
}

export const CardContent: React.FC<CardContentProps> = ({ children }) => {
  return <div className="space-y-3 py-4">{children}</div>
}

interface CardItemProps {
  label: string
  value: string | number
}

export const CardItem: React.FC<CardItemProps> = ({ label, value }) => {
  return (
    <div className="flex justify-between items-start gap-2">
      <span className="text-sm text-gray-600 dark:text-gray-400 font-medium">
        {label}:
      </span>
      <span className="text-sm text-gray-900 dark:text-gray-200 text-right">
        {value}
      </span>
    </div>
  )
}

interface CardFooterProps {
  children: React.ReactNode
}

export const CardFooter: React.FC<CardFooterProps> = ({ children }) => {
  return (
    <div className="flex gap-2 pt-4 border-t border-gray-200 dark:border-dark-700">
      {children}
    </div>
  )
}
