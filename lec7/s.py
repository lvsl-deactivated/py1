# coding: utf-8
import cgi
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
from cStringIO import StringIO

from jinja_example2 import main as example_html


class S(ThreadingMixIn, HTTPServer): pass


class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Encoding', 'utf-8')
        self.end_headers()

        self.wfile.write(example_html())
        self.wfile.write(self.path)
        self.wfile.flush()
        self.connection.close()


    def do_POST(self):
        content_type, pdict = cgi.parse_header(self.headers['content-type'])

        max_chunk_size = 2048
        size_remaining = int(self.headers["content-length"])

        raw_data = ''
        while size_remaining:
            chunk_size = min(size_remaining, max_chunk_size)
            data = self.rfile.read(chunk_size)
            size_remaining -= len(data)
            raw_data = raw_data + data

        request_dict = {}
        is_binary = False
        if 'application/x-www-form-urlencoded' in content_type:
            request_dict = cgi.parse_qs(raw_data)

        elif 'multipart/form-data' in content_type:
            request_dict = cgi.parse_multipart(StringIO(raw_data), pdict)
            is_binary = True

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Content-Encoding', 'utf-8')
        self.end_headers()

        self.wfile.write(raw_data)
        self.wfile.write(request_dict)
        self.wfile.write(is_binary)
        self.wfile.flush()
        self.connection.close()


def main():
    s = S(('', 8080), H)
    s.serve_forever()


if __name__ == "__main__":
    main()
