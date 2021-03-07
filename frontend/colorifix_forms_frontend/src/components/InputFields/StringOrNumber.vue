<template>
  <v-text-field color="rgb(154, 110, 11)"
    v-model="inputVal"
    :rules="parameter.rerquired === 'true' ? [requiredRules, parameter.type === 'string' ? stringRules: numberRules]:[parameter.type === 'string' ? stringRules: numberRules]"
    :label="parameter.label"
    outlined
    dense
  ></v-text-field>
</template>
<script>
export default {
  data: () => {
    return {
      requiredRules: value => !!value || "Required.",
      stringRules: value =>
        /^[A-Za-z ]*$/.test(value) || "Please only add alphabets",
      numberRules: value => /^[0-9]*$/.test(value) || "Please only add a number"
    };
  },
  props: ["parameter", "strOrNum"],
  computed: {
    inputVal: {
        get() {
          return this.strOrNum;
        },
        set(selected) {
          this.$emit('input', selected);
        }
    }
    }
};
</script>

