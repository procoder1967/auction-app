<template>
  <div class="font-sans">
    <NavBar/>
    <SearchBar/>
    <h1 class="font-bold text-3xl px-12">Items Listing</h1>
    <Item/>
    <Item/>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Item from './components/Item.vue';
import NavBar from './components/NavBar.vue';
import SearchBar from './components/SearchBar.vue';

export default defineComponent({
    components: { NavBar, SearchBar, Item }
})
</script>

