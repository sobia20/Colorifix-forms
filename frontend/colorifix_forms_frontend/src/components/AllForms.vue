<template>
  <v-container fluid>
    <v-text-field class="mx-auto filter-size" dark placeholder="Search..." dense v-model="search"></v-text-field>
    <v-card
      v-for="form in filteredForms"
      :key="form.name"
      max-width="500"
      outlined
      hover
      class="mx-auto card-white-space card-overflow-wrap card-spacing"
      color="rgb(255, 168, 20)"
    >
      <router-link
        class="remove-hyperlink-styles"
        :to="{ name: 'formspecs', params: { name: form.name }}"
      >
        <v-card-title>{{ form.label }}</v-card-title>
      </router-link>
    </v-card>
  </v-container>
</template>
<script>
import { socket, socketCheck } from "../plugins/websocket";
import { EventBus } from "../main";

export default {
  name: "AllForms",
  components: {},
  data: () => {
    return {
      listOfForms: [],
      search: ""
    };
  },
  methods: {
    fetchList: function() {
      socket.send('{"action":"get-form-name"}');
      socket.onmessage = message => {
        this.listOfForms = JSON.parse(message.data);
      };
    }
  },
  mounted() {
    socketCheck(this.fetchList);
    EventBus.$emit("label", "Colorifix Forms");
  },
  computed: {
    filteredForms: function() {
      var self = this;
      return this.listOfForms.filter(function(form) {
        return form.label.toLowerCase().indexOf(self.search.toLowerCase()) >= 0;
      });
    }
  }
};
</script>
<style>
.remove-hyperlink-styles {
  color: black !important;
  text-decoration: none !important;
}
.card-spacing {
  margin-top: 10px;
}
.filter-size {
  width: 500px;
}
</style>
