/**
 * CardGrid Component
 * Responsive grid container for displaying multiple cards
 */

import React from 'react'

interface CardGridProps {
  children: React.ReactNode
  columns?: 1 | 2 | 3 | 4
}

export const CardGrid: React.FC<CardGridProps> = ({ children, columns = 3 }) => {
  const gridColsClass = {
    1: 'grid-cols-1',
    2: 'grid-cols-1 md:grid-cols-2',
    3: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-3',
    4: 'grid-cols-1 md:grid-cols-2 lg:grid-cols-4',
  }[columns]

  return (
    <div className={`grid ${gridColsClass} gap-6 w-full`}>
      {children}
    </div>
  )
}
