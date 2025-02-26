<template>
  <div id="app">
    <el-container>
      <el-header>Visual Nginx</el-header>
      <el-container>
        <el-aside width="200px">
          <NginxInfo />
        </el-aside>
        <el-container>
          <NginxConfig />
          <el-main></el-main>
          <el-footer>Created By HopoZ</el-footer>
        </el-container>
      </el-container>
    </el-container>
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