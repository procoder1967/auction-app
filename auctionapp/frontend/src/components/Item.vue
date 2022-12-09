<template>
    <div>
        <div class="content flex mx-20 mt-20">
            <img class="border w-96 h-52">
            <div class="px-4">
                <div class="content flex">
                    <h1 class="font-bold text-lg w-96">Playstations 5 - BRAND NEW</h1>
                    <Message/>
                </div>
                <p class="text-gray-600 h-20">Text text text</p>
                <h3>Top Bider:</h3>
                <h3>Seller:</h3>
                <div class="content flex mb-20">
                    <h3 class="py-2 pr-40">Time Left: 55 min (Fri, 16:55)</h3>
                    <button class="bg-nav-blue hover:bg-blue-700 text-white font-bold py-2 px-6 mr-3 -my-2 rounded-full">Place Bid</button>
                    <input type="text" class="w-12 border rounded">
                    <h1 class="font-bold text-3xl pl-10">£500</h1>
                </div>
            </div>
        </div>
        <hr class="mx-10">
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Message from './Message.vue';

export default defineComponent({
    setup() {
        return {};
    },
    components: { Message }
})
</script>
