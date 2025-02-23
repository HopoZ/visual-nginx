<template>
  <div id="app">
    <NginxInfo />
    <NginxConfig />
  </div>
</template>

<script>
import NginxInfo from './components/nginxInfo.vue';
import NginxConfig from './components/nginxConfig.vue';

export default {
  name: 'App',
  components: {
    NginxInfo,
    NginxConfig,
  },
};
</script>

<style>
/* Add your styles here */
</style>