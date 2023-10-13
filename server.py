import http.server
import socketserver
import json
import builtwith
import random

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = json.loads(post_data)

        # Extract the URL from the request data
        url = data['url']

        # Perform technology detection logic using the builtwith library
        technologies = builtwith.builtwith(url)

        # Convert the detected technologies to JSON format
        response_data = json.dumps(technologies)

        # Set the response headers and send the response
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(response_data.encode('utf-8'))

if __name__ == "__main__":
    PORT = random.randint(8000,8999)
    Handler = RequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Server started at http://localhost:" + str(PORT))
        httpd.serve_forever()
