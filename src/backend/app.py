from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import os
import logging

app = Flask(__name__)
CORS(app)

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

nginx_dir = 'E:/TempZ/extra/nginx-1.27.4'  # 默认 Nginx 目录
nginx_conf_path = os.path.join(nginx_dir, 'conf', 'nginx.conf')  # Nginx 配置文件路径
logger.info(f"nginx_conf_path: {nginx_conf_path}")

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
        logger.info(f"Nginx status output: {status_output}")

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
    try:
        with open(nginx_conf_path, 'r') as file:
            config = file.read()
        return config
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/update_nginx_config', methods=['POST'])
def update_nginx_config():
    try:
        config = request.json.get('config')
        if not request.is_json:
            return {"error": "Request must be in JSON format"}, 400
        config = request.json.get('config')
        if config is None:
            return {"error": "Missing 'config' field in JSON data"}, 400
        if not os.path.exists(os.path.dirname(nginx_conf_path)):
            return {"error": f"Directory {os.path.dirname(nginx_conf_path)} does not exist"}, 400
        if not os.access(os.path.dirname(nginx_conf_path), os.W_OK):
            return {"error": f"No write permission for {os.path.dirname(nginx_conf_path)}"}, 400
        with open(nginx_conf_path, 'w') as file:
            file.write(config)
        # subprocess.run(['nginx', '-s', 'reload', '-c', nginx_conf_path], check=True, cwd=nginx_dir)
        return {"message": "Configuration updated successfully"}
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/nginx_dir', methods=['POST'])
def set_nginx_dir():
    global nginx_dir, nginx_conf_path
    nginx_dir = request.json.get('nginx_dir')
    nginx_conf_path = os.path.join(nginx_dir, 'conf', 'nginx.conf')
    logger.info(f"Nginx directory set to {nginx_dir}")
    logger.info(f"Nginx config path set to {nginx_conf_path}")
    return {"message": f"Nginx directory set to {nginx_dir}"}

@app.route('/api/get_nginx_dir', methods=['GET'])
def get_nginx_dir():
    return jsonify({"nginx_dir": nginx_dir})

@app.route('/api/nginx/start', methods=['POST'])
def start_nginx():
    try:
        subprocess.run([nginx_dir,'nginx', '-c', nginx_conf_path], check=True)
        return {"message": "Nginx started successfully"}
    except Exception as e:
        return {"error": str(e)}, 500

@app.route('/api/nginx/stop', methods=['POST'])
def stop_nginx():
    try:
        result = subprocess.run(['nginx', '-s', 'stop'], check=True, capture_output=True, text=True, cwd=nginx_dir)
        logger.info(f"Stop Nginx output: {result.stdout}")
        logger.info(f"Stop Nginx error output: {result.stderr}")
        return {"message": "Nginx stopped successfully"}
    except subprocess.CalledProcessError as e:
        logger.error(f"CalledProcessError: {e}")
        logger.error(f"Output: {e.output}")
        logger.error(f"Error output: {e.stderr}")
        return {"error": f"Failed to stop Nginx: {e}"}, 500
    except Exception as e:
        logger.error(f"Exception: {e}")
        return {"error": str(e)}, 500

@app.route('/api/nginx/reload', methods=['POST'])
def reload_nginx():
    try:
        subprocess.run(['nginx', '-s', 'reload', '-c', nginx_conf_path], check=True, cwd=nginx_dir)
        return {"message": "Nginx reloaded successfully"}
    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8082, debug=True)
