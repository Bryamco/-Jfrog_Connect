"""
Hello World - Aplicación simple para demostrar despliegue en JFrog Container Registry.
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

PORT = int(os.getenv("PORT", "8080"))


class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        html = """<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>Hello World</title>
<style>
  body { font-family: sans-serif; display: flex; justify-content: center;
         align-items: center; height: 100vh; margin: 0;
         background: linear-gradient(135deg, #41BF47 0%, #007BFF 100%); color: #fff; }
  .card { text-align: center; background: rgba(0,0,0,.25); padding: 3rem 4rem;
          border-radius: 16px; }
  h1 { font-size: 3rem; margin-bottom: .5rem; }
  p  { font-size: 1.2rem; opacity: .85; }
</style></head>
<body>
  <div class="card">
    <h1>🐸 ¡Hola Mundo!</h1>
    <p>Desplegado con <strong>JFrog Container Registry</strong></p>
  </div>
</body>
</html>"""
        self.wfile.write(html.encode())

    def log_message(self, fmt, *args):
        print(f"[REQUEST] {args[0]}")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), HelloHandler)
    print(f"🚀 Servidor escuchando en http://0.0.0.0:{PORT}")
    server.serve_forever()
