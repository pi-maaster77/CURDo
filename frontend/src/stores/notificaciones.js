import { defineStore } from 'pinia'

export const useNotificacionesStore = defineStore('notificaciones', {
  state: () => ({
    mensajes: []
  }),

  actions: {
    push(tipo, texto, timeout = 4000) {
      const n = { tipo, texto }
      this.mensajes.push(n)

      setTimeout(() => {
        const i = this.mensajes.indexOf(n)
        if (i !== -1) this.mensajes.splice(i, 1)
      }, timeout)
    },

    error(texto, timeout) {
      this.push('error', texto, timeout)
    },

    success(texto, timeout) {
      this.push('success', texto, timeout)
    },

    clear(i) {
      this.mensajes.splice(i, 1)
    }
  }
})
