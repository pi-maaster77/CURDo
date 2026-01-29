import { defineStore } from 'pinia'
import { fetchTags, createTag, updateTag, deleteTag } from '@/api/tags'

export const useTagsStore = defineStore('tags', {
  state: () => ({
    tags: [],
    cargando: false
  }),

  getters: {
    getTag: state => id =>
      state.tags?.find(t => t.id == id)
  },

  actions: {
    async optimistic(mutator, request) {
      const backup = [...this.tags]

      try {
        mutator()
        await request()
      } catch (e) {
        this.tags = backup
        console.error(e)
      }
    },

    async cargar() {
      this.cargando = true
      try {
        this.tags = await fetchTags()
      } finally {
        this.cargando = false
      }
    },

    async crear({ nombre, color_id }) {
      const cid = crypto.randomUUID()

      await this.optimistic(
        () => {
          this.tags.push({
            id: cid,
            nombre,
            color: {
              rojo: 0,
              verde: 0,
              azul: 0
            },
            _optimistic: true
          })
        },
        async () => {
          const real = await createTag({ nombre, color_id })
          console.log('Respuesta del servidor:', real)
          const idx = this.tags.findIndex(t => t.id === cid)
          if (idx !== -1) {
            this.tags[idx] = real
            console.log('Tag actualizado con ID real:', real.id)
          }
        }
      )
    },


    async editar({ id, nombre, color_id }) {
      await this.optimistic(
        () => {
          const i = this.tags.findIndex(t => t.id === id)
          if (i !== -1) {
            const updated = { ...this.tags[i] }

            if (nombre !== undefined) {
              updated.nombre = nombre
            }

            if (color_id !== undefined) {
              updated.color_id = color_id
            }

            this.tags[i] = updated
          }
        }, 
        async () => {
          const real = await updateTag({ id, nombre, color_id })
          const i = this.tags.findIndex(t => t.id === id)
          console.log(real)
          if (i !== -1) this.tags[i] = real
        }
      )
    },

    async eliminar(id) {
      await this.optimistic(
        () => {
          this.tags = this.tags.filter(t => t.id !== id)
        },
        () => deleteTag(id)
      )
    }
  }
})
