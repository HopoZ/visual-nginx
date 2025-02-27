<template>
    <div style="box-shadow:inset 0 0 10px #000000; padding: 20px;">
        <h2>Nginx Information</h2>
        <p>Nginx is a high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server. It is known
            for
            its high performance, stability, rich feature set, simple configuration, and low resource consumption.</p>
        <h2>Version</h2>
        <p>Nginx version: 1.18.0-alpine</p>

        <h2>Runtime Information</h2>
        <div v-if="status">
            <p>Accepted Connections: {{ status.accepted_connections }}</p>
            <p>Active Connections: {{ status.active_connections }}</p>
            <p>Handled Connections: {{ status.handled_connections }}</p>
            <p>Total Requests: {{ status.total_requests }}</p>
            <p>Reading Connections: {{ status.reading_connections }}</p>
            <p>Writing Connections: {{ status.writing_connections }}</p>
            <p>Waiting Connections: {{ status.waiting_connections }}</p>
        </div>
        <div v-else>
            Loading...
        </div>
    </div>
</template>

<script>
import { fetchNginxStatus } from '../api';
import { ref } from 'vue';

export default {
    data() {
        return {
            status: null,
        };
    },
    async mounted() {
        try {
            this.status = await fetchNginxStatus();
        } catch (error) {
            console.error('Error fetching Nginx status:', error);
        }
    },
};
</script>