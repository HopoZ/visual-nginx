from flask import Flask, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

def get_nginx_status():
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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8082, debug=True)
