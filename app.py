import os
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer

# --- your script code here ---
def main_script():
    while True:
        print("Running my bot/script...")
        time.sleep(10)  # replace with your real code

# --- minimal web server for Koyeb health check ---
PORT = int(os.environ.get("PORT", 8000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_web_server():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Healthcheck server running on port {PORT}")
    server.serve_forever()

if __name__ == "__main__":
    # Run your script in a background thread
    threading.Thread(target=main_script, daemon=True).start()
    
    # Start the web server (for Koyeb)
    run_web_server()
