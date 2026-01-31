/* eslint-disable no-unused-vars */

import api from "./base"

const baseUrl = `/api/tags`

export const fetchTags = async () =>
  (await api.get(`${baseUrl}/`)).data

export const createTag = async ({ nombre, color_id }) =>
  (await api.post(`${baseUrl}/`, { nombre, color: color_id })).data

export const updateTag = async ({ id, nombre, color_id }) =>
  (await api.patch(`${baseUrl}/${id}`, { nombre, color: color_id })).data

export const deleteTag = async (id) =>
  (await api.delete(`${baseUrl}/${id}`)).data
