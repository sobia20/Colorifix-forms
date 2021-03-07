<template>
  <v-container fluid>
    <v-card flat outlined class="mx-auto card-margin card-background text-color">
      <v-card-title>{{ form_details.description }}</v-card-title>
      <v-card-subtitle class="card-subtitle-font-size">{{ $route.params.name }}</v-card-subtitle>
      <v-form ref="form" class="form-padding" lazy-validation>
        <div v-for="parameter in form_details.parameters" :key="parameter.name">
          <Select
            v-if="parameter.type == 'select'"
            :parameter="parameter" select=""
            v-model="formSubmit[parameter.name]"
          />
          <StringOrNumber
            v-if="parameter.type == 'string' || parameter.type == 'number'"
            :parameter="parameter" strOrNum=""
            v-model="formSubmit[parameter.name]"
          />
          <Checkbox
            v-if="parameter.type == 'bool'"
            :parameter="parameter" checked=""
            v-model="formSubmit[parameter.name]"
          />
        </div>
        <v-snackbar v-model="snackbar" :timeout="timeout" absolute>
          {{ snackbarText }}
          <template v-slot:action="{ attrs }">
            <v-btn  class="text-color" text v-bind="attrs" @click="snackbar = false">Close</v-btn>
          </template>
        </v-snackbar>
        <v-btn @click="validate" style="float:right" dark>Submit</v-btn>
      </v-form>
    </v-card>
  </v-container>
</template>
<script>
import { socket, socketCheck } from "../plugins/websocket";
import { EventBus } from "../main";
import Select from "./InputFields/Select";
import StringOrNumber from "./InputFields/StringOrNumber";
import Checkbox from "./InputFields/Checkbox";

export default {
  data: () => {
    return {
      form_details: {},
      formSubmit: {},
      snackbar: false,
      timeout: 2000,
      snackbarText: "There is an error in submitting the form.",
      clicked:false
    };
  },
  components: {
    Select,
    StringOrNumber,
    Checkbox
  },
  methods: {
    validate() {
      if (this.$refs.form.validate() && this.clicked==false) {
        this.snackbar = true;
        this.formSubmit["form_name"] = this.form_details.name;
        this.formSubmit["action"] = "submit-form";
        this.formSubmit = JSON.stringify(this.formSubmit);
        socket.send(this.formSubmit);
        socket.onmessage = message => {
          console.log(message.data);
        };
        this.snackbarText = "Your form has been successfully submitted";
        this.formSubmit = {};
        this.clicked = true;
      }
      else if(this.clicked){
        this.snackbar = true;
        this.snackbarText = "You have already submitted the form."
      }
    },
    fetchSpecs() {
      socket.send(
        `{"action":"get-form-specs","name": "${this.$route.params.name}"}`
      );
      socket.onmessage = message => {
        this.form_details = JSON.parse(message.data);
        EventBus.$emit("label", this.form_details.label);
      };
    }
  },
  mounted() {
    socketCheck(this.fetchSpecs);
  }
};
</script>
<style>
.card-margin {
  width: 500px;
  margin-top: 10px;
  padding-bottom: 34px;
}
.card-subtitle-font-size {
  font-size: 16px !important;
  font-weight: 500 !important;
}
.form-padding {
  padding-left: 16px;
  padding-right: 20px;
  padding-top: 16px;
  padding-bottom: 16px;
}

.card-background{
    background-color: #f0ff72 !important;
}
</style>
