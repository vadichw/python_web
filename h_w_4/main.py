import json
import pathlib
import socketserver
import socket
import threading
import urllib.parse
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime


BASE_DIR = pathlib.Path()


class HTTPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        body = urllib.parse.unquote_plus(body.decode())
        payload = {key: value for key, value in [el.split('=') for el in body.split('&')]}

        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            server_address = ('localhost', 5000)
            sock.sendto(json.dumps(payload).encode(), server_address)

        self.send_response(302)
        self.send_header('Location', '/')
        self.end_headers()

    def do_GET(self):
        route = urllib.parse.urlparse(self.path)
        match route.path:
            case "/":
                self.send_html('index.html')
            case "/message":
                self.send_html('message.html')
            case _:
                file = BASE_DIR / route.path[1:]
                if file.exists():
                    self.send_static(file)
                else:
                    self.send_error(404, "Not Found")

    def send_html(self, filename, status_code=200):
        self.send_response(status_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as f:
            self.wfile.write(f.read())

    def send_static(self, filename):
        self.send_response(200)
        mime_type, _ = mimetypes.guess_type(filename)
        if mime_type:
            self.send_header('Content-Type', mime_type)
        else:
            self.send_header('Content-Type', 'text/plain')
        self.end_headers()
        
        with open(filename, 'rb') as f:
            self.wfile.write(f.read())


class SocketHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data, _ = self.request
        payload = json.loads(data.decode())

        # Adding timestamp to payload
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

        # Save data to data.json
        with open(BASE_DIR.joinpath('storage/data.json'), 'a', encoding='utf-8') as fd:
            json.dump({timestamp: payload}, fd, ensure_ascii=False)
            fd.write('\n')


def run_http_server():
    address = ('', 3000)
    http_server = HTTPServer(address, HTTPHandler)
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()


def run_socket_server():
    address = ('', 5000)
    socket_server = socketserver.UDPServer(address, SocketHandler)
    socket_thread = threading.Thread(target=socket_server.serve_forever)
    socket_thread.start()
    socket_thread.join()


if __name__ == '__main__':

    http_thread = threading.Thread(target=run_http_server)
    socket_thread = threading.Thread(target=run_socket_server)

    http_thread.start()
    socket_thread.start()

    http_thread.join()
    socket_thread.join()

