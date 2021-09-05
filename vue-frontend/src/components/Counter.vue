<template>
  <div>
    <p>Current count: {{count}}</p> 
    <button v-on:click="count+=1">increment</button>
    <button v-on:click="count-=1" v-if="count>0" >decrement</button> 
  </div>  
</template>

//dont want a negative count so us if. as of now I only know how to make the whole button appear or dissapear based on Count.


<script>
export default {
  data() {
    return {
      count: 0
    };
  }
};
</script>

<style>
</style>

