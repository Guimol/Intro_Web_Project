<script setup>
import { ref } from 'vue';
import easy_json from '../assets/QuincasBorbas_Short_Easy.json';
import hard_json from '../assets/QuincasBorbas_Short_Hard.json';

defineProps({
  msg: String,
});

const count = ref(0);
</script>

<script>
export default {
  data() {
    return {
      list_tokens: [],
      difficulty: 'Hard',
      array: [],
      array_index: 0,
    };
  },
  methods: {
    iterate_counter() {
      this.count = this.count + 1;
    },
  },
  computed: {
    nextList() {
      if (this.array_index < this.list_tokens.length - 10) {
        this.array = this.list_tokens.slice(
          this.array_index,
          this.array_index + 10
        );
      }
      this.array_index++;
    },

    showList() {
      if (this.difficulty == 'Hard') {
        this.list_tokens = hard_json.book[this.count].text.split(' ');
      } else {
        this.list_tokens = easy_json.book[this.count].text.split(' ');
      }

      return this.list_tokens;
    },
  },
};
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

  <button type="button" @click="iterate_counter()">
    Next Chapter {{ count }}
  </button>
  <p>{{ hard_json.book.title }}</p>
  <p>{{ hard_json.book[count].chapter }}</p>
  <!--<p>{{ hard_json.book[count].text.split(' ') }}</p>-->
  <p>{{ showList }}</p>
  <button type="button" @click="nextList">Next List</button>
  <p>{{ array }}</p>
  <p>Indice {{ array_index }}</p>
  <button type="button" @click="count--">Previous Chapter</button>
  <button type="button" @click="count = 0">Reset Chapter index</button>
  <!--TODO: Check last chapter-->
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
