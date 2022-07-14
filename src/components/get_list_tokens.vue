<script setup>
import { ref } from 'vue';
import easy_json from '../assets/QuincasBorbas_Short_Easy.json';
import hard_json from '../assets/QuincasBorbas_Short_Hard.json';

defineProps({
  msg: String,
});

const count = ref(-1);
</script>

<script>
export default {
  data() {
    return {
      book: easy_json.book,
      list_tokens: [],
      difficult: false,
      array_10_tokens: [],
      array_10_tokens_index: 0,
    };
  },
  methods: {
    new_chapter() {
      let random = Math.floor(
        Math.random() * Object.keys(this.book).length - 1
      );

      while (random == this.count || random < 0) {
        random = Math.floor(Math.random() * Object.keys(this.book).length - 1);
      }
      this.count = random;
    },

    change_difficulty() {
      this.difficult = !this.difficult;
      if (this.difficult) {
        this.book = this.hard_json.book;
      } else {
        this.book = this.easy_json.book;
      }
    },

    nextList() {
      if (this.array_10_tokens_index < this.list_tokens.length - 10) {
        this.array_10_tokens = this.list_tokens.slice(
          this.array_10_tokens_index,
          this.array_10_tokens_index + 10
        );
      }
      this.array_10_tokens_index++;
    },
  },
  computed: {
    show_text() {
      this.list_tokens = this.book[this.count].text.split(' ');
      return this.list_tokens.join(' ');
    },

    show_10_token_array() {
      return this.array_10_tokens.join(' ');
    },
  },
  beforeMount() {
    this.new_chapter();
    this.nextList();
  },
};
</script>

<template>
  <h1>{{ msg }}</h1>
  <p>{{ this.book.title }}</p>
  <p>{{ this.book[this.count].chapter }}</p>

  <button type="button" @click="new_chapter()">New Chapter</button>
  <button type="button" @click="change_difficulty()">
    Make it {{ difficult ? 'Easy' : 'Hard' }}
  </button>

  <p>{{ show_text }}</p>
  <button type="button" @click="nextList">Next 10 token array</button>
  <p>{{ show_10_token_array }}</p>
  <p>Indice {{ array_10_tokens_index }}</p>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
