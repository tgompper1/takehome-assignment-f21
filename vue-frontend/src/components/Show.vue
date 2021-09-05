<template>
  <!-- PART 4: Add your code here -->
  <div id="container">
    <h4>{{name}}</h4>
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
h4{
  margin-top: 25px;
  font-weight: bold;
}
</style>
