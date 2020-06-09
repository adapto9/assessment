<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <h1>Upload CSV</h1>
        <v-file-input accept=".csv" label="File input" v-model="file"></v-file-input>
        <v-btn block color="primary" v-on:click="submitFile()" :loading="loading">Submit</v-btn>
        <blockquote class="blockquote">{{ response }}</blockquote>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      file: null,
      loading: false,
      response: ""
    };
  },

  methods: {
    submitFile() {
      if (this.file != null) {
        this.loading = true;
        let formData = new FormData();
        formData.append("file", this.file);
        axios
          .post("http://127.0.0.1:5000/users/upload", formData, {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          })
          .then(response => {
            this.response = response.data.results;
            this.file = null;
            this.loading = false
          })
          .catch(error => {
            this.response =
              "Error code " +
              error.response.status +
              ": " +
              error.response.data.results;
            this.file = null;
            this.loading = false
          });
      }
    }
  }
};
</script>
