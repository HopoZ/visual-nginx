<template>
    <div>
        <h2>Modify Nginx Configuration</h2>
        <div ref="editor"></div>
        <el-button type="primary" @click="updateConfig">Update Configuration</el-button>
        <br><br>
        <h2>Nginx Control</h2>
        <el-input v-model="nginxDir" placeholder="Enter Nginx Directory"></el-input>
        <el-button type="primary" @click="setNginxDir">Set Nginx Directory</el-button>
        <br><br>
        <div style="box-shadow:inset 0 0 10px blue;">Current Nginx Directory: {{ currentNginxDir }}</div>
        <br><br>
        <div>
            <el-button type="success" @click="startNginx">Start Nginx</el-button>
            <el-button type="warning" @click="stopNginx">Stop Nginx</el-button>
            <el-button type="info" @click="reloadNginx">Reload Nginx</el-button>
        </div>
    </div>
</template>

<script>
import { fetchNginxConfig, updateNginxConfig, setNginxDir, getNginxDir, startNginx, stopNginx, reloadNginx } from '../api';
import CodeMirror from 'codemirror';
import 'codemirror/lib/codemirror.css';
import 'codemirror/mode/nginx/nginx'; // 引入 Nginx 语法高亮
import { ElMessage } from 'element-plus';

export default {
    data() {
        return {
            config: '',
            nginxDir: '',
            currentNginxDir: '',
            editor: null,
        };
    },
    mounted() {
        fetchNginxConfig()
            .then(data => {
                this.config = data;
                this.initCodeMirror();
            })
            .catch(error => {
                console.error('Error fetching Nginx configuration:', error);
            });
        getNginxDir()
            .then(data => {
                this.currentNginxDir = data.nginx_dir;
            })
            .catch(error => {
                console.error('Error fetching Nginx directory:', error);
            });
    },
    methods: {
        initCodeMirror() {
            this.editor = CodeMirror(this.$refs.editor, {
                value: this.config,
                mode: 'nginx',
                lineNumbers: true,
                matchBrackets: true,
                autoCloseBrackets: true,
                theme: 'default',
            });
            this.editor.on('change', () => {
                this.config = this.editor.getValue();
            });
        },
        updateConfig() {
            updateNginxConfig(this.config)
                .then(data => {
                    ElMessage({
                        message: 'Nginx configuration updated successfully',
                        type: 'success',
                    });
                })
                .catch(error => {
                    console.error('Error updating Nginx configuration:', error);
                    ElMessage.error('Oops, this is a error message.Go to check the console log and contact HopoZ');
                });
        },
        setNginxDir() {
            setNginxDir(this.nginxDir)
                .then(data => {
                    this.currentNginxDir = this.nginxDir;
                    alert('Nginx directory set successfully');
                })
                .catch(error => {
                    console.error('Error setting Nginx directory:', error);
                });
        },
        startNginx() {
            startNginx()
                .then(data => {
                    alert('Nginx started successfully');
                })
                .catch(error => {
                    console.error('Error starting Nginx:', error);
                });
        },
        stopNginx() {
            stopNginx()
                .then(data => {
                    alert('Nginx stopped successfully');
                })
                .catch(error => {
                    console.error('Error stopping Nginx:', error);
                });
        },
        reloadNginx() {
            reloadNginx()
                .then(data => {
                    alert('Nginx reloaded successfully');
                })
                .catch(error => {
                    console.error('Error reloading Nginx:', error);
                });
        },
    },
};
</script>

<style>
.CodeMirror {
    border: 1px solid #ccc;
}
</style>