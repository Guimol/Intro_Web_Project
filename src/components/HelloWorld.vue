<script setup>
import { ref } from 'vue';
import hard_json from '../assets/QuincasBorbas_Short_Hard.json';

defineProps({
  msg: String,
});

const count = ref(0);
</script>

<template>
  <h1>{{ msg }}</h1>

  <p>
    Recommended IDE setup:
    <a href="https://code.visualstudio.com/" target="_blank">VS Code</a>
    +
    <a href="https://github.com/johnsoncodehk/volar" target="_blank">Volar</a>
  </p>

  <p>
    <a href="https://vitejs.dev/guide/features.html" target="_blank">
      Vite Documentation
    </a>
    |
    <a href="https://v3.vuejs.org/" target="_blank">Vue 3 Documentation</a>
  </p>

  <button type="button" @click="count++">Next Chapter</button>
  <p>{{ hard_json.book.title }}</p>
  <p>{{ hard_json.book[count].chapter }}</p>
  <p>{{ hard_json.book[count].text }}</p>
  <button type="button" @click="count--">Previous Chapter</button>
  <button type="button" @click="count = 0">Reset Chapter index</button>
  <!--TODO: Check last chapter-->
  <p>
    Edit
    <code>components/HelloWorld.vue</code> to test hot module replacement.
  </p>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
