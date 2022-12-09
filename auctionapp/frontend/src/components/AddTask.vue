<template>
<div>
  <a class="py-2 px-3 hover:text-red-500 cursor-pointer" @click="showModal = true">+ Add Task</a>

  <BaseModal :show="showModal">
    <div class="p-4">
      <div>
        <label for="title">Item's Title</label><br>
        <input class="border" type="text" required>
      </div>
      <div>
        <label for="item" >Description</label><br>
        <textarea class="border" rows = "5" cols = "50" placeholder="Enter your item's description." required></textarea>
      </div>
      <div>
        <label for="image" >Image</label><br>
        <input type="file" name="item_img">
      </div>
      <div>
        <label for="bidEnd" >Time bid finishes</label><br>
        <input class="border" type="datetime-local" name="date">
      </div>
      <div>
        <label for="price" >Starting price</label><br>
        <input class="border" type="number" name="date">
      </div>

      <button type="button" class="bg-indigo-200 px-3 py-1 font-medium mx-2" @click="showModal = false">
        Submit
      </button>
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

