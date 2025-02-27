<template>
  <div id="app" style="height: 100vh;width: 100vw;">
    <el-container style="height: 100vh;width: 100vw;">
      <el-header>
        <div class="flip-title">Visual Nginx</div>
      </el-header>
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
  flex-shrink: 20;
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


.flip-title {
  font-size: 60px;
  font-family: Arial, sans-serif;
  color: #000000;
  transform-style: preserve-3d;
  transform-origin: center;
  animation: flip 3s infinite;
  padding: 0px;
  box-shadow: 0 0 0 2px transparent;
  /* animation: flip 3s infinite, border-gradient 4s infinite linear; */
}

@keyframes flip {
  0% {
    transform: rotateX(0deg);
  }

  50% {
    transform: rotateX(180deg);
  }

  100% {
    transform: rotateX(360deg);
  }
}

@keyframes border-gradient {
  0% {
    box-shadow: 0 0 0 2px #ff00cc;
  }

  25% {
    box-shadow: 0 0 0 2px #00ffcc;
  }

  50% {
    box-shadow: 0 0 0 2px #00ccff;
  }

  75% {
    box-shadow: 0 0 0 2px #cc00ff;
  }

  100% {
    box-shadow: 0 0 0 2px #ff00cc;
  }
}
</style>