import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_API_URL || '',
  headers: { 'X-Requested-With': 'XMLHttpRequest' },
  withCredentials: true,
})

export default api

