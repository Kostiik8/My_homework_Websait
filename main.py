from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Если запрашивается корневая страница, отправляем контактную страницу
        if self.path == "/":
            self.path = "/contact.html"

        # Определение полного пути к файлу
        file_path = self.path[1:]

        # Попытка найти и отправить файл
        try:
            # Открываем файл и читаем его содержимое
            with open(file_path, "rb") as file:
                self.send_response(200)

                # Определяем тип контента
                if self.path.endswith(".html"):
                    self.send_header("Content-type", "text/html")
                elif self.path.endswith(".css"):
                    self.send_header("Content-type", "text/css")
                elif self.path.endswith(".js"):
                    self.send_header("Content-type", "application/javascript")
                elif self.path.endswith(".svg"):
                    self.send_header("Content-type", "image/svg+xml")
                elif self.path.endswith(".png"):
                    self.send_header("Content-type", "image/png")
                elif self.path.endswith(".jpg") or self.path.endswith(".jpeg"):
                    self.send_header("Content-type", "image/jpeg")
                else:
                    self.send_header("Content-type", "application/octet-stream")

                self.end_headers()
                self.wfile.write(file.read())  # Отправляем файл клиенту
        except:
            # Если файл не найден, отправляем 404
            self.send_response(404)
            self.end_headers()
            self.wfile.write(bytes("404 Not Found", "utf-8"))


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Server started http://{hostName}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
