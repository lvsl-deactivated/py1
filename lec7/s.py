# coding: utf-8

from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn

from jinja_example2 import main as example_html


class S(ThreadingMixIn, HTTPServer): pass


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Encoding', 'utf-8')
        self.end_headers()

        self.wfile.write(example_html())
        self.wfile.flush()
        self.connection.close()


def main():
    s = S(('', 8080), H)
    s.serve_forever()


if __name__ == "__main__":
    main()
