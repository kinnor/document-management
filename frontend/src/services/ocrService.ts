export async function extractText(file: File): Promise<string> {
  const formData = new FormData()
  formData.append('file', file)

  const resp = await fetch('/extract', {
    method: 'POST',
    body: formData,
  })

  if (!resp.ok) {
    let detail = 'Upload failed'
    try {
      const data = await resp.json()
      detail = data.detail || detail
    } catch {}
    throw new Error(detail)
  }

  const data = await resp.json()
  return data.text
}
