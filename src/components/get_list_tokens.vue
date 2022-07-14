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
      input: '',
      variable: 'Eu não fui mudada',
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
      this.array_10_tokens_index = 0;
      this.next_10_tokens_array();
    },

    change_difficulty() {
      this.difficult = !this.difficult;
      if (this.difficult) {
        this.book = this.hard_json.book;
      } else {
        this.book = this.easy_json.book;
      }
      this.array_10_tokens_index = 0;
      this.next_10_tokens_array();
    },

    next_10_tokens_array() {
      this.list_tokens = this.book[this.count].text.split(' ');

      if (this.array_10_tokens_index < this.list_tokens.length - 10) {
        this.array_10_tokens = this.list_tokens.slice(
          this.array_10_tokens_index,
          this.array_10_tokens_index + 10
        );
      }
      this.array_10_tokens_index++;
    },

    minha_func() {
      this.variable = 'Bla Bla Bla';
    },
  },
  computed: {
    show_text() {
      return this.list_tokens.join(' ');
    },

    show_10_token_array() {
      return this.array_10_tokens.join(' ');
    },
  },
  beforeMount() {
    this.new_chapter();
    this.array_10_tokens_index = 0;
    this.list_tokens = this.book[this.count].text.split(' ');
    this.next_10_tokens_array();
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
  <button type="button" @click="next_10_tokens_array()">
    Next 10 token array
  </button>
  <p>{{ show_10_token_array }}</p>
  <input
    v-model="input"
    :placeholder="[[show_10_token_array]]"
    v-on:keyup.space="minha_func"
  />
  <p>Variavel: {{ variable }}</p>
  <p>Escrito: {{ input }}</p>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
