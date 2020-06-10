<template>
  <v-container>
    <v-row class="text-center">
      <v-col cols="12">
        <h1 class="display-2 font-weight-bold mb-3">Dashboard</h1>
        <blockquote class="blockquote">{{ response }}</blockquote>
      </v-col>

      <v-col cols="12">
        <v-card flat>
          <v-container grid-list-xl text-xs-center>
            <v-layout row wrap>
              <v-flex xs6>
                <v-text-field v-model="minSalary" label="Minimum Salary"></v-text-field>
              </v-flex>
              <v-flex xs6>
                <v-text-field v-model="maxSalary" label="Maximum Salary"></v-text-field>
              </v-flex>
              <v-flex xs6>
                <v-select v-model="sortColumn" :items="columns" label="Sort By"></v-select>
              </v-flex>
              <v-flex xs6>
                <v-select v-model="sortOrder" :items="orders" label="Order"></v-select>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card>
        <v-btn block color="primary" v-on:click="populate(false)" :loading="loading">Search</v-btn>
      </v-col>

      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="employees"
          :loading="loading"
          :page.sync="page"
          :items-per-page="limit"
          hide-default-footer
          class="elevation-1"
        ></v-data-table>
        <div class="text-center pt-2">
          <v-pagination v-model="page" :length="pageCount"></v-pagination>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "Dashboard",

  data: () => ({
    headers: [
      {
        text: "Id",
        align: "start",
        sortable: false,
        value: "id"
      },
      { text: "Login", sortable: false, value: "login" },
      { text: "Name", sortable: false, value: "name" },
      { text: "Salary", sortable: false, value: "salary" }
    ],
    page: 1,
    pageCount: 0,
    minSalary: 0,
    maxSalary: 5000,
    offset: 0,
    limit: 30,
    sortColumn: "Id",
    sortOrder: "Ascending",
    employees: [],
    response: null,
    loading: false,
    columns: ["Id", "Login", "Name", "Salary"],
    orders: ["Ascending", "Descending"]
  }),
  computed: {
    sort: function() {
      if (this.sortOrder == "Ascending") {
        return "+" + this.sortColumn.toLowerCase();
      } else {
        return "-" + this.sortColumn.toLowerCase();
      }
    }
  },
  watch: {
    page: function() {
      this.offset = (this.page - 1) * this.limit;
      this.populate(true);
    }
  },
  methods: {
    populate(newPage) {
      this.loading = true;
      axios
        .get("http://127.0.0.1:5000/users", {
          params: {
            minSalary: this.minSalary,
            maxSalary: this.maxSalary,
            offset: this.offset,
            limit: this.limit,
            sort: this.sort
          }
        })
        .then(response => {
          this.loading = false;
          if (newPage == false) {
            if (response.data.count[0][0] % this.limit != 0) {
              console.log(response.data.count[0][0])
              this.pageCount = Math.floor(response.data.count[0][0] / this.limit) + 1;
            } else {
              this.pageCount = Math.floor(response.data.count[0][0] / this.limit);
            }
          }

          this.employees = response.data.results;
        })
        .catch(error => {
          this.loading = false;
          this.response =
            "Error code " +
            error.response.status +
            ": " +
            error.response.data.results;
        });
    }
  },
  mounted() {
    this.populate(false);
  }
};
</script>
