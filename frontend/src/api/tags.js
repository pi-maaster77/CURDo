/* eslint-disable no-unused-vars */

import axios from 'axios';

const baseUrl = `/api/tags`

export const fetchTags = async () =>
  (await axios.get(`${baseUrl}/`)).data

export const createTag = async ({ nombre, color_id }) =>
  (await axios.post(`${baseUrl}/`, { nombre, color: color_id })).data

export const updateTag = async ({ id, nombre, color_id }) =>
  (await axios.patch(`${baseUrl}/${id}`, { nombre, color: color_id })).data

export const deleteTag = async (id) =>
  (await axios.delete(`${baseUrl}/${id}`)).data
