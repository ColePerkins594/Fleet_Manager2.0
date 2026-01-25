/**
 * SkeletonCard Component
 * Displays a loading skeleton while data is being fetched
 */

interface SkeletonCardProps {
  count?: number
}

export const SkeletonCard: React.FC<SkeletonCardProps> = ({ count = 1 }) => {
  return (
    <>
      {Array.from({ length: count }).map((_, index) => (
        <div
          key={index}
          className="card p-6 space-y-4"
        >
          {/* Header Skeleton */}
          <div className="flex items-start justify-between gap-4">
            <div className="flex-1 space-y-3">
              <div className="h-6 bg-gray-200 dark:bg-dark-700 rounded-md w-3/4 animate-pulse" />
              <div className="h-4 bg-gray-200 dark:bg-dark-700 rounded-md w-1/2 animate-pulse" />
            </div>
            <div className="h-8 w-20 bg-gray-200 dark:bg-dark-700 rounded-md animate-pulse" />
          </div>

          {/* Content Skeleton */}
          <div className="space-y-3 pt-2">
            <div className="h-4 bg-gray-200 dark:bg-dark-700 rounded-md animate-pulse" />
            <div className="h-4 bg-gray-200 dark:bg-dark-700 rounded-md w-5/6 animate-pulse" />
            <div className="h-4 bg-gray-200 dark:bg-dark-700 rounded-md w-4/6 animate-pulse" />
          </div>

          {/* Footer Skeleton */}
          <div className="flex gap-2 pt-4">
            <div className="h-8 flex-1 bg-gray-200 dark:bg-dark-700 rounded-md animate-pulse" />
            <div className="h-8 flex-1 bg-gray-200 dark:bg-dark-700 rounded-md animate-pulse" />
          </div>
        </div>
      ))}
    </>
  )
}
