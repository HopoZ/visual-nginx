export async function fetchNginxStatus() {
    try {
        const response = await fetch('http://localhost:8082/api/nginx_status');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching Nginx status:', error);
        throw error;
    }
}

export async function fetchNginxConfig() {
    try {
        const response = await fetch('http://localhost:8082/api/nginx_config');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.text();
        return data;
    } catch (error) {
        console.error('Error fetching Nginx configuration:', error);
        throw error;
    }
}

export async function updateNginxConfig(config) {
    try {
        const response = await fetch('http://localhost:8082/api/update_nginx_config', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ config }),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error updating Nginx configuration:', error);
        throw error;
    }
}

export async function setNginxDir(nginxDir) {
    try {
        const response = await fetch('http://localhost:8082/api/nginx_dir', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ nginx_dir: nginxDir }),
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error setting Nginx directory:', error);
        throw error;
    }
}
export async function getNginxDir() {
    try {
        const response = await fetch('http://localhost:8082/api/get_nginx_dir', {
            method: 'GET',
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching Nginx directory:', error);
        throw error;
    }
}

export async function startNginx() {
    try {
        const response = await fetch('http://localhost:8082/api/nginx/start', {
            method: 'POST',
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error starting Nginx:', error);
        throw error;
    }
}

export async function stopNginx() {
    try {
        const response = await fetch('http://localhost:8082/api/nginx/stop', {
            method: 'POST',
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error stopping Nginx:', error);
        throw error;
    }
}

export async function reloadNginx() {
    try {
        const response = await fetch('http://localhost:8082/api/nginx/reload', {
            method: 'POST',
        });
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error reloading Nginx:', error);
        throw error;
    }
}