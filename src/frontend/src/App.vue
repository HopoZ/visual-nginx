<template>
  <div id="app" style="height: 100vh;width: 100vw;">
    <el-container>
      <el-header>Visual Nginx</el-header>
      <el-container>
        <el-aside width="200px">
          <NginxInfo />
        </el-aside>
        <el-container>
          <el-main>
            <NginxConfig />
          </el-main>
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
html,
body,
#app {
  height: 100%;
  margin: 0;
}

#app {
  display: flex;
  flex-direction: column;
}

.el-container {
  display: flex;
  flex: 1;
}

.el-header,
.el-footer {
  flex-shrink: 0;
  text-align: center;
  /* Center the text in header and footer */
}

.el-aside {
  flex-shrink: 0;
}

.el-main {
  flex: 1;
  overflow: auto;
  display: flex;
  justify-content: center;
  /* Center the content horizontally */
  align-items: center;
  /* Center the content vertically */
  flex-direction: column;
  /* Ensure the content is in a column */
}
</style>