<template>
  <div class="upload">
    <div class="container">
      <div class="large-12 medium-12 small-12 cell">
        <h1>Upload Employees CSV</h1>
        <label>
          File
          <input type="file" id="file" ref="file" v-on:change="handleFileUpload()" />
        </label>
        <button v-on:click="submitFile()">Submit</button>
        <div class="response">{{ response }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      file: "",
      response: ""
    };
  },

  methods: {
    submitFile() {
      let formData = new FormData();
      formData.append("file", this.file);
      axios
        .post("http://127.0.0.1:5000/users/upload", formData, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(response => {
          this.response = response;
          this.file = "";
        })
        .catch(response => {
          this.response = response;
          this.file = "";
        });
    },

    handleFileUpload() {
      this.file = this.$refs.file.files[0];
    }
  }
};
</script>
