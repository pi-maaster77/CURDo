import axios from 'axios'

const baseUrl = `/api/asociar`
export const asociarTagAElemento = async (elementoId, tagId) =>
  axios.post(`${baseUrl}/elementos/${elementoId}/tags/${tagId}`)

export const desasociarTagDeElemento = async (elementoId, tagId) =>
  axios.delete(`${baseUrl}/elementos/${elementoId}/tags/${tagId}`)
