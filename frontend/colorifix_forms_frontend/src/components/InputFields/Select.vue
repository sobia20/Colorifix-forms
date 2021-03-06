<template>
<v-select
    v-model="inputVal"
    :label="parameter.label"
    :items="parameter.options"
    outlined
    dense
    :rules="parameter.rerquired == 'true' ? [required] : []"
    ></v-select>
</template>
<script>
export default {
    props:["parameter", "select"],
    data: () => {
        return {
            required: value => !!value || false
        }
    },
    computed: {
        inputVal: {
            get() {
                return this.select;
            },
            set(selected) {
                this.$emit('input', selected);
            }
        }
    }
}
</script>

    