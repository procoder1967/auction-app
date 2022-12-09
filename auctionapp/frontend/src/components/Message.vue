<template>
    <div>
        <img @click="showModal = true" src="../assets/text.png" class="w-8 h-8 mx-60 cursor-pointer">
    <BaseModal :show="showModal">
        <div class="p-4">
        <div>
            <label for="item" >Message</label><br>
            <textarea class="border" rows = "5" cols = "50" placeholder="Enter message." required></textarea>
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
    setup () {
        const showModal = ref(false);
        return{showModal}
    }
})
</script>
