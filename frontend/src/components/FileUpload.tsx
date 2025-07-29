import React, { useState } from 'react'
import axios from 'axios'
import { extractText, OCRResult } from '../services'
import ResultDisplay from './ResultDisplay'

const MAX_SIZE = 5 * 1024 * 1024 // 5MB

function FileUpload() {
  const [file, setFile] = useState<File | null>(null)
  const [error, setError] = useState('')
  const [result, setResult] = useState<OCRResult | null>(null)
  const [loading, setLoading] = useState(false)

  const onFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setResult(null)
    const selected = e.target.files?.[0] || null
    if (!selected) {
      setFile(null)
      return
    }
    if (selected.type !== 'application/pdf') {
      setError('Please select a PDF file.')
      setFile(null)
      return
    }
    if (selected.size > MAX_SIZE) {
      setError('File size must be less than 5MB.')
      setFile(null)
      return
    }
    setError('')
    setFile(selected)
  }

  const onUpload = async () => {
    if (!file) {
      setError('No file selected.')
      return
    }
    setError('')
    setLoading(true)
    try {
      const data = await extractText(file)
      setResult(data)
    } catch (err: any) {
      if (axios.isAxiosError(err)) {
        setError(err.response?.data?.detail || err.message)
      } else {
        setError(err.message)
      }
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="upload-container">
      <input type="file" accept="application/pdf" onChange={onFileChange} />
      <button onClick={onUpload} disabled={loading}>
        {loading ? 'Uploading...' : 'Upload'}
      </button>
      {error && <p className="error">{error}</p>}
      {result && <ResultDisplay data={result} />}
    </div>
  )
}

export default FileUpload

