from http.server import HTTPServer, BaseHTTPRequestHandler
import json


class MyServer(BaseHTTPRequestHandler):

    # GET: Home endpoint
    def do_GET(self):

        response = {
            "message": "Welcome to Python DevFlow!",
            "status": "Server is running",
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(response).encode("utf-8"))

    # POST: Register endpoint
    def do_POST(self):

        content_length = int(self.headers["Content-Length"])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode("utf-8"))
        token = self.headers["token"]
        print(token)
        # token_data = self.rfile.read(token)
        # points = json.loads(token_data.decode("utf-8"))
        # print(token, token_data, points)

        if self.path == "/register":
            if data["name"]:
                print(data["name"])
            else:
                print("not found")

            if "email" in data:

                if data["email"]:
                    print(data["email"])
                    response = {
                        "message": "Registration successful!",
                        "user": {
                            "id": 101,
                            "username": data.get("username"),
                            "email": data.get("email"),
                        },
                    }
                else:
                    response = {"message": "Email Value Missing"}
                    self.send_response(201)

            else:
                response = {"message": "Email Key Missing"}
                self.send_response(201)

        elif self.path == "/login":

            response = {
                "message": "Login successful!",
                "user": {"id": 101, "email": data.get("email")},
                "token": "dummy-token-12345",
            }

            self.send_response(200)

        else:
            self.send_error(404, "Endpoint not found")
            return

        self.send_header("Content-Type", "application/json")
        self.end_headers()

        self.wfile.write(json.dumps(response).encode("utf-8"))


server = HTTPServer(("localhost", 8000), MyServer)

print("Server running on http://localhost:8000")

server.serve_forever()
