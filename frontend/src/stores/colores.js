import { defineStore } from 'pinia'
import { createColor, fetchColors, updateColor, deleteColor } from '@/api/color'

export const useColorsStore = defineStore('colores', {
  state: () => ({
    colores: [],
    cargando: false
  }),

  getters: {
    getColor: state => id =>
      state.colores.find(c => c.id === id)
  },

  actions: {
    async optimistic(mutator, request) {
      const backup = [...this.colores]

      try {
        mutator()
        await request()
      } catch (e) {
        this.colores = backup
        throw e
      }
    },

    async cargar() {
      this.cargando = true
      try {
        this.colores = await fetchColors()
      } finally {
        this.cargando = false
      }
    },

    async crear({ nombre, rojo, verde, azul }) {
      const cid = crypto.randomUUID()

      await this.optimistic(
        () => {
          this.colores.push({
            id: cid,
            nombre,
            rojo,
            verde,
            azul,
            _optimistic: true
          })
        },
        async () => {
          const real = await createColor(nombre, rojo, verde, azul)
          const i = this.colores.findIndex(c => c.id === cid)
          if (i !== -1) this.colores[i] = real
        }
      )
    },

    async editar({ id, nombre, rojo, verde, azul }) {
      await this.optimistic(
        () => {
          const i = this.colores.findIndex(c => c.id === id)
          if (i !== -1) {
            this.colores[i] = {
              ...this.colores[i],
              ...(nombre !== undefined && { nombre }),
              ...(rojo !== undefined && { rojo }),
              ...(verde !== undefined && { verde }),
              ...(azul !== undefined && { azul })
            }
          }
        },
        async () => {
          const real = await updateColor(id, nombre, rojo, verde, azul)
          const i = this.colores.findIndex(c => c.id === id)
          if (i !== -1) this.colores[i] = real
        }
      )
    },

    async eliminar(id) {
      await this.optimistic(
        () => {
          this.colores = this.colores.filter(c => c.id !== id)
        },
        () => deleteColor(id)
      )
    }
  }
})
