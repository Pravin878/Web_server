from http.server import HTTPServer,BaseHTTPRequestHandler

content='''
Hello
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)  
        self.send_header('content-type', 'text/html; charset=utf-8')      
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()