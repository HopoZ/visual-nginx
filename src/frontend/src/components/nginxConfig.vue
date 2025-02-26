<template>
    <div>
        <h1>Modify Nginx Configuration</h1>
        <textarea v-model="config" rows="20" cols="80"></textarea>
        <br>
        <el-button type="primary" @click="updateConfig">Update Configuration</el-button>
        <br><br>
        <h2>Nginx Control</h2>
        <el-input v-model="nginxDir" placeholder="Enter Nginx Directory"></el-input>
        <el-button type="primary" @click="setNginxDir">Set Nginx Directory</el-button>
        <br><br>
        <el-button type="success" @click="startNginx">Start Nginx</el-button>
        <el-button type="warning" @click="stopNginx">Stop Nginx</el-button>
        <el-button type="info" @click="reloadNginx">Reload Nginx</el-button>
    </div>
</template>

<script>
import { fetchNginxConfig, updateNginxConfig, setNginxDir, startNginx, stopNginx, reloadNginx } from '../api';

export default {
    data() {
        return {
            config: '',
            nginxDir: '',
        };
    },
    mounted() {
        fetchNginxConfig()
            .then(data => {
                this.config = data;
            })
            .catch(error => {
                console.error('Error fetching Nginx configuration:', error);
            });
    },
    methods: {
        updateConfig() {
            updateNginxConfig(this.config)
                .then(data => {
                    alert('Configuration updated successfully');
                })
                .catch(error => {
                    console.error('Error updating Nginx configuration:', error);
                });
        },
        setNginxDir() {
            setNginxDir(this.nginxDir)
                .then(data => {
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