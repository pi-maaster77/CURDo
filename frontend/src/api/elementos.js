import api from "./base"

const baseUrl = `/api/elementos`

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

  const url = search.toString() ? `${baseUrl}/?${search.toString()}` : baseUrl
  return (await api.get(url)).data
}

export const createElemento = async ({ nombre }) =>
  (await api.post(`${baseUrl}/`, { nombre })).data

export const updateElemento = async (id, data) =>
  (await api.patch(`${baseUrl}/${id}`, data)).data

export const deleteElemento = async (id) =>
  (await api.delete(`${baseUrl}/${id}`)).data
