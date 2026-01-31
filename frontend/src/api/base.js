import axios from "axios";

const api = axios.create({
  baseURL: 'https://api.curdo.xyz',
  timeout: 10000,
})

export default api
