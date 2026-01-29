import axios from 'axios';

const baseUrl = `${process.env.VUE_APP_API_URL || 'http://localhost:8000'}/api/elementos`
const baseUrlAsociar = `${process.env.VUE_APP_API_URL || 'http://localhost:8000'}/api/asociar`

export const fetchElementos = async (params = {}) =>
  (await axios.get(baseUrl, { params })).data

export const createElemento = async (nombre) =>
  (await axios.post(baseUrl, { nombre })).data

export const updateElemento = async (id, data) =>
  (await axios.patch(`${baseUrl}/${id}`, data)).data

export const deleteElemento = async (id) =>
  (await axios.delete(`${baseUrl}/${id}`)).data

export const asociarTagAElemento = async (elementoId, tagId) =>
  (await axios.post(`${baseUrlAsociar}/elementos/${elementoId}/tags/${tagId}`)).data

export const desasociarTagDeElemento = async (elementoId, tagId) =>
  (await axios.delete(`${baseUrlAsociar}/elementos/${elementoId}/tags/${tagId}`)).data
