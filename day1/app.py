import http.server
from datadog import initialize, statsd

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}


APP_PORT = 8000

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # creating count increment metrics 
        statsd.increment('ashuapp.http.request.count', sample_rate=1, tags =["env:ashudev" ,"ashuapp:pythonapp"])
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>First Application</title></head><body style='color: #333; margin-top: 30px;'><center><h2>Welcome to Datadog-Python application.</center></h2></body></html>", "utf-8"))

if __name__ == "__main__":
    initialize(**options)
    server = http.server.HTTPServer(('0.0.0.0', APP_PORT), HandleRequests)
    server.serve_forever()
