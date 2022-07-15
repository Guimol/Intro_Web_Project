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
      valid: false,
      count_correct: 0,
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

    verify_text() {
      this.valid = this.input.trim() == this.array_10_tokens[0];
      this.input = ''; //Limpar o input form
      if (this.valid) {
        this.count_correct++;
      }
      this.next_10_tokens_array();
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
  <div id="corpo" class="container-md pt-3 pb-5">
    <div id="descricao" class="border border-4 rounded m-5">
      <h2>Quão rápido você consegue digitar?</h2>
      <h4>Copie o texto mostrado na tela que te diremos!</h4>
      <p>
        Texto extraído de {{ this.book.title }},
        {{ this.book[this.count].chapter }}
      </p>
    </div>

    <p>{{ show_text }}</p>

    <form class="row justify-content-center">
      <div class="col-md-8 mb-3">
        <input
          type="text"
          class="form-control"
          v-model="input"
          :placeholder="[[show_10_token_array]]"
          v-on:keyup.space="verify_text"
        />
      </div>
    </form>

    <button
      type="button"
      class="btn-dark border border-2"
      @click="new_chapter()"
    >
      Outro Capítulo
    </button>
    <button
      type="button"
      class="btn-dark border border-2"
      @click="change_difficulty()"
    >
      Dificuldade {{ difficult ? 'Fácil' : 'Difícil' }}
    </button>
    <button
      type="button"
      class="btn-dark border border-2"
      @click="next_10_tokens_array()"
    >
      Próxima Linha
    </button>
    <p>{{ show_10_token_array }}</p>
    <!-- Quero fazer que ao dar um espaço troque a palavra atual e sempre fique fazendo a computação de onde esta errado e limpar o input-->

    <p>{{ valid ? 'Acertou' : 'Errou' }}</p>
    <p>Source: {{ input }}</p>
    <p>Target: {{ array_10_tokens[0] }}</p>
    <p>Acertos: {{ count_correct }}/{{ list_tokens.length }}</p>

    <div
      id="selfpromotion"
      class="card-deck row m-auto d-flex justify-content-center text-dark"
    >
      <h2 style="color: #aec3b0">Quem Somos</h2>
      <div class="card col-md-3">
        <img
          class="card-img-top mt-3"
          src="https://avatars.githubusercontent.com/u/36967571?v=4"
        />
        <div class="card-body">
          <h5 class="card-title">Milan Rufini</h5>
          <p class="card-text">
            Adora jogar Minecraft e fazer arte. Futuro cientista da computação.
          </p>
        </div>
        <div class="card-footer">
          <small class="text-muted">
            <a href="mailto:rufini@usp.br">Contato</a>
          </small>
        </div>
      </div>

      <div name="spacer" class="card col-md-3 invisible">
        <p class="card-text">???</p>
      </div>

      <div class="card col-md-3">
        <img
          class="card-img-top mt-3"
          src="https://avatars.githubusercontent.com/u/51828246?v=4"
        />
        <div class="card-body">
          <h5 class="card-title">Guilherme Martiniano</h5>
          <p class="card-text">
            Estudante de ciência da computação, gosta de jogar tênis e jogos
            online.
          </p>
        </div>
        <div class="card-footer">
          <small class="text-muted">
            <a href="mailto:guizera11@usp.br">Contato</a>
          </small>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
a {
  color: #42b983;
}
</style>
