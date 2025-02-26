from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)

nginx_dir = 'E:/TempZ/extra/nginx-1.27.4'  # 默认 Nginx 目录

def get_nginx_status():
    if os.name == 'nt':  # Windows
        nginx_status_url = "http://localhost/nginx_status"
    else:  # Unix/Linux
        nginx_status_url = "http://nginx:80/nginx_status"

    try:
        # Use curl to get Nginx status information
        status_output = subprocess.check_output(["curl", "-s", nginx_status_url], text=True)
        lines = status_output.strip().split("\n")

        # Log the status output for debugging
        print("Nginx status output:", status_output)

        # Check if the lines list has the expected number of elements
        if len(lines) < 4:
            return {"error": "Unexpected Nginx status output format"}

        # Parse Nginx status
        # Active connections line
        active_connections = int(lines[0].split(":")[1].strip())

        # Parsing the 'server accepts handled requests' line
        # Skip the second line
        server_line = lines[2].strip().split()
        accepted, handled, total_requests = map(int, server_line[:3])

        # Parsing the 'Reading: X Writing: Y Waiting: Z' line
        reading_connections, writing_connections, waiting_connections = map(int, lines[3].split()[1::2])

        return {
            "active_connections": active_connections,
            "accepted_connections": accepted,
            "handled_connections": handled,
            "total_requests": total_requests,
            "reading_connections": reading_connections,
            "writing_connections": writing_connections,
            "waiting_connections": waiting_connections
        }
    except subprocess.CalledProcessError as e:
        return {"error": f"Failed to get Nginx status: {e}"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/api/nginx_status', methods=['GET'])
def nginx_status():
    return jsonify(get_nginx_status())

@app.route('/api/nginx_config', methods=['GET'])
def get_nginx_config():
    if os.name == 'nt':  # Windows
        config_path = os.path.join(nginx_dir, 'conf', 'nginx.conf')
    else:  # Unix/Linux
        config_path = '/etc/nginx/conf.d/default.conf'

    try:
        with open(config_path, 'r') as file:
            config = file.read()
        return config
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/nginx_config', methods=['POST'])
def update_nginx_config():
    if os.name == 'nt':  # Windows
        config_path = os.path.join(nginx_dir, 'conf', 'nginx.conf')
    else:  # Unix/Linux
        config_path = '/etc/nginx/conf.d/default.conf'

    try:
        config = request.json.get('config')
        with open(config_path, 'w') as file:
            file.write(config)
        subprocess.run(['nginx', '-s', 'reload'])
        return {"message": "Configuration updated successfully"}
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/nginx_dir', methods=['POST'])
def set_nginx_dir():
    global nginx_dir
    nginx_dir = request.json.get('nginx_dir')
    return {"message": f"Nginx directory set to {nginx_dir}"}

@app.route('/api/nginx/start', methods=['POST'])
def start_nginx():
    try:
        subprocess.run([os.path.join(nginx_dir, 'nginx.exe')])
        return {"message": "Nginx started successfully"}
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/nginx/stop', methods=['POST'])
def stop_nginx():
    try:
        subprocess.run([os.path.join(nginx_dir, 'nginx.exe'), '-s', 'stop'])
        return {"message": "Nginx stopped successfully"}
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/nginx/reload', methods=['POST'])
def reload_nginx():
    try:
        subprocess.run([os.path.join(nginx_dir, 'nginx.exe'), '-s', 'reload'])
        return {"message": "Nginx reloaded successfully"}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8082, debug=True)
