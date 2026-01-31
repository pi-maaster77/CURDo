import api from "./base"

const baseUrl = `/api/asociar`
export const asociarTagAElemento = async (elementoId, tagId) =>
  api.post(`${baseUrl}/elementos/${elementoId}/tags/${tagId}`)

export const desasociarTagDeElemento = async (elementoId, tagId) =>
  api.delete(`${baseUrl}/elementos/${elementoId}/tags/${tagId}`)
