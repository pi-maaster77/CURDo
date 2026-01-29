import axios from 'axios';

const baseUrl = `${process.env.VUE_APP_API_URL || 'http://localhost:8000'}/api/elementos`

export const fetchElementos = async (params = {}) => {
  // Build query string so arrays are sent as repeated keys: tag=1&tag=2
  const search = new URLSearchParams()

  Object.entries(params || {}).forEach(([k, v]) => {
    if (v === undefined || v === null) return
    if (Array.isArray(v)) {
      v.forEach(val => search.append(k, val))
    } else {
      search.append(k, String(v))
    }
  })

  const url = search.toString() ? `${baseUrl}?${search.toString()}` : baseUrl
  return (await axios.get(url)).data
}

export const createElemento = async ({ nombre }) =>
  (await axios.post(baseUrl, { nombre })).data

export const updateElemento = async (id, data) =>
  (await axios.patch(`${baseUrl}/${id}`, data)).data

export const deleteElemento = async (id) =>
  (await axios.delete(`${baseUrl}/${id}`)).data
