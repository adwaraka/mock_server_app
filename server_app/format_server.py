from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from format_file import FileFormat
import ast, json

class FileHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET( self ):
        line = self.path.lstrip("/")
        self._set_headers()
        fileformat = FileFormat()
        paragraph = fileformat.format_file()
        data = {}

        for i in xrange(len(paragraph)):
            data[str(i)] = paragraph[i]

        try:
            self.wfile.write(json.dumps(data[str(line)]))
        except KeyError:
            self.wfile.write(json.dumps(data))

def run():
    server_address = ('127.0.0.1', 3001)
    httpd = HTTPServer(server_address, FileHandler)
    print "FileHandler server is running....."
    httpd.serve_forever()

if __name__== "__main__":
    run()
