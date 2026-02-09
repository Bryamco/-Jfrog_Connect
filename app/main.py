"""
Hello World - App simple para JFrog Container Registry.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = int(os.getenv("PORT", "8080"))

HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Hello World</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{min-height:100vh;display:grid;place-items:center;
  background:#0f0f0f;color:#fff;font-family:system-ui,sans-serif}
.container{text-align:center;animation:fade .8s ease}
h1{font-size:4rem;margin-bottom:.5rem}
p{font-size:1.1rem;color:#888}
span{color:#41BF47}
@keyframes fade{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}
</style>
</head>
<body>
  <div class="container">
    <h1>Hello World <span>🐸</span></h1>
    <p>Desplegado en <span>JFrog</span> desde GitHub Actions</p>
  </div>
</body>
</html>"""


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML.encode())

    def log_message(self, *_): pass


if __name__ == "__main__":
    print(f"🚀 http://localhost:{PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
