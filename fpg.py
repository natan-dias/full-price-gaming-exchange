from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

PRICES = {
    'BRL': 399,
    'USD': 70,
    'EUR': 70,
}


def calculate_games(amount, currency):
    fpg = PRICES.get(currency.upper(), 70)
    return round(amount / fpg, 2)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            base = os.path.dirname(os.path.abspath(__file__))
            with open(os.path.join(base, 'index.html'), 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == '/calculate':
            length = int(self.headers['Content-Length'])
            body = json.loads(self.rfile.read(length))
            amount = float(body['amount'])
            currency = body['currency']
            result = calculate_games(amount, currency)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'result': result}).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        pass


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8000), Handler)
    print('Server running at http://localhost:8000')
    server.serve_forever()
