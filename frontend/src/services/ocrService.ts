import api from './api'

export async function extractText(file: File): Promise<string> {
  const formData = new FormData()
  formData.append('file', file)

  try {
    const resp = await api.post('/extract', formData)
    return resp.data.text as string
  } catch (err: any) {
    const detail = err.response?.data?.detail || err.message || 'Upload failed'
    throw new Error(detail)
  }
}

