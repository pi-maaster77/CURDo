/* eslint-disable no-unused-vars */
import api from "./base"

const baseUrl = `/api/colores`

export const fetchColors = async () =>
  (await api.get(`${baseUrl}/`)).data

export const createColor = async (nombre, rojo, verde, azul) =>
  (await api.post(`${baseUrl}/`, { nombre, rojo, verde, azul })).data

export const updateColor = async (id, nombre) =>
  (await api.patch(`${baseUrl}/${id}`, { nombre })).data

export const deleteColor = async (id) =>
  (await api.delete(`${baseUrl}/${id}`)).data
