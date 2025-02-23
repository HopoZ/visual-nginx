<template>
    <div>
        <h1>Modify Nginx Configuration</h1>
        <textarea v-model="config" rows="20" cols="80"></textarea>
        <br>
        <button @click="updateConfig">Update Configuration</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            config: '',
        };
    },
    mounted() {
        fetch('http://localhost:8082/api/nginx_config')
            .then(response => response.text())
            .then(data => {
                this.config = data;
            })
            .catch(error => {
                console.error('Error fetching Nginx configuration:', error);
            });
    },
    methods: {
        updateConfig() {
            fetch('http://localhost:8082/api/nginx_config', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ config: this.config }),
            })
                .then(response => response.json())
                .then(data => {
                    alert('Configuration updated successfully');
                })
                .catch(error => {
                    console.error('Error updating Nginx configuration:', error);
                });
        },
    },
};
</script>