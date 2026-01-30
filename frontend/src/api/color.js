/* eslint-disable no-unused-vars */

import axios from 'axios'

const baseUrl = `/api/colores`

export const fetchColors = async () =>
  (await axios.get(`${baseUrl}/`)).data

export const createColor = async (nombre, rojo, verde, azul) =>
  (await axios.post(`${baseUrl}/`, { nombre, rojo, verde, azul })).data

export const updateColor = async (id, nombre) =>
  (await axios.patch(`${baseUrl}/${id}`, { nombre })).data

export const deleteColor = async (id) =>
  (await axios.delete(`${baseUrl}/${id}`)).data
