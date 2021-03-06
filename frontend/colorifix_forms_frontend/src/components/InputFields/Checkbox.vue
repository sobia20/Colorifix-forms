<template>
  <v-checkbox
    v-model="inputVal"
    :rules="parameter.rerquired == 'true' ? [required] : []"
    :label="parameter.label"
    color="rgb(255, 168, 20)"
  ></v-checkbox>
</template>
<script>
export default {
    data: () => {
    return {
        required: value => !!value || "Required." 
    }
    },
    props:["parameter", "checked"],
    computed: {
        inputVal: {
        get() {
            return this.checked;
        },
        set(check) {
            this.$emit('input', check);
        }
        }
  }
}
</script>

