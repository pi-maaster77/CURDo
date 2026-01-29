
import { defineStore } from 'pinia'
import { fetchElementos, createElemento, updateElemento, deleteElemento } from '@/api/elementos'
import { asociarTagAElemento, desasociarTagDeElemento } from '@/api/elementoTags'
export const useElementosStore = defineStore('elementos', {
  state: () => ({
    elementos: [],
  }),

  getters: {
    getElemento: state => id =>
      state.elementos.find(e => e.id === id)
  },

  actions: {
    async optimistic(fn, request) {
      const backup = [...this.elementos]

      try {
        fn()
        await request()
      } catch (e) {
        this.elementos = backup
        console.error(e)
      }
    },

    async cargar(filtros = {}) {
      // Mapear los filtros del front (tags, tagMode, checked)
      // al formato que espera la API (tag, tag_mode, checked)
      const params = {}

      if (filtros.tags && Array.isArray(filtros.tags) && filtros.tags.length > 0) {
        params.tag = filtros.tags
      }

      if (filtros.tagMode) {
        params.tag_mode = filtros.tagMode
      }

      if (filtros.checked !== undefined) {
        params.checked = filtros.checked
      }

      this.elementos = await fetchElementos(params)
    },
    async crear(nombre) {
      const temp = {
        id: crypto.randomUUID(),
        nombre,
        _optimistic: true
      }

      await this.optimistic(
        () => {
          this.elementos.push(temp)
        },
        async () => {
          console.log(nombre)
          const real = await createElemento({nombre})
          const idx = this.elementos.findIndex(e => e.id === temp.id)
          if (idx !== -1) this.elementos[idx] = real
        }
      )
    },

    async editar(elemento) {
      await this.optimistic(
        () => {
          const i = this.elementos.findIndex(e => e.id === elemento.id)
          if (i !== -1) {
            this.elementos[i] = { ...this.elementos[i], ...elemento }
          }
        },
        () => updateElemento(elemento.id, elemento)
      )
    },
    async toggleChecked(id, checked) {
      await this.optimistic(
        () => {
          const i = this.elementos.findIndex(e => e.id === id)
          if (i !== -1) this.elementos[i].checked = checked
        },
        () => updateElemento( id, {checked} )
      )
    },
    async eliminar(id) {
      await this.optimistic(
        () => {
          this.elementos = this.elementos.filter(e => e.id !== id)
        },
        () => deleteElemento(id)
      )
    },
    async actualizarTags(elementoId, nuevasTags) {
      const elemento = this.elementos.find(e => e.id === elementoId)
      if (!elemento) return

      const tagsActuales = elemento.tags ?? []

      const aAgregar = nuevasTags.filter(id => !tagsActuales?.includes(id))
      const aQuitar  = tagsActuales.filter(id => !nuevasTags?.includes(id))

      // optimistic update
      elemento.tags = nuevasTags

      try {
        await Promise.all([
          ...aAgregar.map(tagId =>
            asociarTagAElemento(elementoId, tagId)
          ),
          ...aQuitar.map(tagId =>
            desasociarTagDeElemento(elementoId, tagId)
          )
        ])
      } catch (e) {
        console.error('Error actualizando tags', e)
        // opcional: rollback
        elemento.tags = tagsActuales
      }
    }
  }
})
