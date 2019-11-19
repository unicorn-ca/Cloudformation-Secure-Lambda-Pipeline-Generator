import os, webbrowser
import sys
import time
from multiprocessing import Process
# import herd
from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(open('index.html', 'rb').read())
        elif os.path.basename(self.path) in ['full-stack.template.yaml']:
            self.send_response(200)
            self.send_header('Content-Type', 'text/yaml')
            self.end_headers()
            self.wfile.write(open(self.path[1:], 'rb').read())
        elif self.path.split('/')[1] in ["css", "js", "img"]:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(open(self.path[1:], 'rb').read())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not found')

    def do_POST(self):
        if self.path == '/deploy':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            # do something with post_data
            config = {}

            # herd.run_deployments(config)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')


def start_server():
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    p1 = Process(target=start_server)
    p1.start()

    os.system("cmd.exe /C 'start http://127.0.0.1:8000'")
    url = "http://127.0.0.1:8000"
    webbrowser.open_new(url)
    
    # print("Error no default browser found on your device. To view the wizard open a browser and go to 'http://127.0.0.1:8000' cheers")
        