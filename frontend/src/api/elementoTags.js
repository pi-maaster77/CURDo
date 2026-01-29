import axios from 'axios'

const baseUrl = `${process.env.VUE_APP_API_URL || 'http://localhost:8000'}/api/asociar`

export const asociarTagAElemento = async (elementoId, tagId) =>
  axios.post(`${baseUrl}/elementos/${elementoId}/tags/${tagId}`)

export const desasociarTagDeElemento = async (elementoId, tagId) =>
  axios.delete(`${baseUrl}/elementos/${elementoId}/tags/${tagId}`)
