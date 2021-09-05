<template>
  <!-- PART 4: Add your code here -->
  <div>
    {{name}}
    <Counter v-bind:initial_count="episodes_seen"></Counter>
  </div>
</template>

<script>
// PART 4: Add your code here

import Counter from "./Counter.vue";

export default {
  props:{
    id: Number,
    name: String,
    episodes_seen: Number
  },
  components:{
    Counter
  }
};
</script>

<style>
</style>
