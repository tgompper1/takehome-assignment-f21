<template>
  <div>
    <p>Episodes watched: {{initial_count}}</p> 
    <button v-on:click="initial_count+=1">increment</button>
    <button v-on:click="initial_count-=1" v-if="initial_count>0" >decrement</button> 
  </div>  
</template>

//dont want a negative count so us if. as of now I only know how to make the whole button appear or dissapear based on Count.
//not sure how to set count as initial count and then update from there, so i replaced count with initial count

<script>
export default {
  data() {
    return {
      initial_count
    };
  },
  props: {
    initial_count: Number
  }
};
</script>

<style>
  button{
    background-color:#eb8686;
    color: #fff;
    border-radius: 10px;
  }
</style>

