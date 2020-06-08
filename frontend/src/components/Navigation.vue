<template>
  <v-container>
    <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense>
        <router-link to="/">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-view-dashboard</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Dashboard</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
        <router-link to="/upload">
          <v-list-item link>
            <v-list-item-action>
              <v-icon>mdi-publish</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Upload</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </router-link>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-left>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>TechHunt 2020</v-toolbar-title>
    </v-app-bar>
  </v-container>
</template>

<style scoped>
a {
  text-decoration: none;
}
</style>

<script>
export default {
  data: () => ({
    drawer: null
  })
};
</script>