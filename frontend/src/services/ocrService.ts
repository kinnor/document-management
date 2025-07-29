import api from './api'

export interface OCRResult {
  text: string
}

export async function extractText(file: File): Promise<OCRResult> {
  const formData = new FormData()
  formData.append('file', file)

  try {
    const resp = await api.post('/extract', formData)
    return resp.data as OCRResult
  } catch (err: any) {
    const detail = err.response?.data?.detail || err.message || 'Upload failed'
    throw new Error(detail)
  }
}

