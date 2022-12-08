<template>
<div>
  <a class="py-2 px-3 hover:text-red-500 cursor-pointer" @click="showModal = true">+ Add Task</a>

  <BaseModal :show="showModal">
    <div class="p-4">
      <div class="text-lg">Hello Modal World!</div>

      <div class="py-2 text-sm">Click to close:</div>

      <button type="button" class="bg-indigo-200 px-3 py-1 font-medium" @click="showModal = false">
        Hide modal
      </button>
    </div>
  </BaseModal>
</div>
</template>

<script lang="ts">
import { defineComponent, ref} from 'vue'
import BaseModal from './modals/BaseModal.vue'

export default defineComponent({
    components: {BaseModal},
    setup(){
        const showModal = ref(false);
        return{showModal}
    },
})
</script>

