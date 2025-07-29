import React from 'react'

interface ResultDisplayProps {
  data: any
}

function ResultDisplay({ data }: ResultDisplayProps) {
  if (!data) return null

  const formatted = JSON.stringify(data, null, 2)

  return (
    <div className="json-output">
      <h3>OCR Result</h3>
      <pre>{formatted}</pre>
    </div>
  )
}

export default ResultDisplay
