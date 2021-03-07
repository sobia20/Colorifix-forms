<template>
  <v-app>
    <v-app-bar dense dark app>
      <v-spacer/>
      <v-toolbar-title style="font-weight: 500;">{{heading}}</v-toolbar-title>
      <v-spacer/>
    </v-app-bar>
    <v-main>
      <v-img
        class="background-brightness"
        height="90vh"
        src="https://colorifix.com/app/uploads/2019/09/aaron-burden-00QWN1J0g48-unsplash-2560x1831.jpg"
      >
        <router-view></router-view>
      </v-img>
    </v-main>
    <v-footer dark padless>
      <v-col class="text-center gold-heading" cols="12">
        <span class="white--text">
          {{ new Date().getFullYear() }} —
          <strong>Colorifix</strong>
        </span>
      </v-col>
    </v-footer>
  </v-app>
</template>
<script>
import { EventBus } from "../main";

export default {
  name: "Layout",
  components: {},
  data: () => {
    return {
      heading: "Colorifix Forms"
    };
  },
  updated() {
    EventBus.$on("label", message => {
      this.heading = message;
    });
  }
};
</script>
<style>
.v-image__image {
  filter: brightness(60%);
}
.colorifix-color {
  color: rgb(255, 168, 20);
}
</style>
