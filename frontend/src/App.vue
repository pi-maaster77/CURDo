<template>
  <div class="container-fluid mt-3">
    <ul class="nav nav-tabs custom-notebook" role="tablist">
      <li class="nav-item">
        <button 
          class="nav-link" 
          :class="{ active: tabActiva === 'elementos' }"
          @click="tabActiva = 'elementos'"
          type="button"
        >
          <i class="bi bi-table me-2"></i>Elementos
        </button>
      </li>
      <li class="nav-item">
        <button 
          class="nav-link" 
          :class="{ active: tabActiva === 'tags' }"
          @click="tabActiva = 'tags'"
          type="button"
        >
          <i class="bi bi-tags me-2"></i>Gestión de Tags
        </button>
      </li>
    </ul>

    <div class="tab-content border-start border-end border-bottom bg-white p-4 shadow-sm">
      <div v-if="tabActiva === 'elementos'" class="tab-pane fade show active">
        <IndexPage />
      </div>

      <div v-if="tabActiva === 'tags'" class="tab-pane fade show active">
        <EditorTags />
      </div>
    </div>
  </div>
  <GlobalError />
</template>

<script setup>
import { ref } from 'vue'
import IndexPage from './views/IndexPage.vue';
import EditorTags from './views/EditorTags.vue';
import GlobalError from './components/domain/GlobalError.vue';
import 'bootstrap-icons/font/bootstrap-icons.min.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.bundle.min.js'
const tabActiva = ref('elementos')
</script>

<style scoped>
/* Estilo para que parezca más una interfaz de escritorio (Notebook) */
.custom-notebook .nav-link {
  color: #6c757d;
  border-radius: 8px 8px 0 0;
  cursor: pointer;
  font-weight: 500;
  padding: 10px 20px;
}

.custom-notebook .nav-link.active {
  color: #0d6efd;
  background-color: #fff;
  border-bottom-color: #fff; /* "Funde" la pestaña con el contenido */
}

.tab-content {
  min-height: 400px;
  border-radius: 0 0 8px 8px;
}
</style>