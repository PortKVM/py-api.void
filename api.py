print("PyAPI (By PortKVM) | Note: If you run the file by itself, it wont work at all and would output an error")

class Response:
    def __init__(self, status_code, headers, body):
        self.status_code = status_code
        self.headers = headers
        self.body = body

class API:
    def __init__(self, base_url):
        self.base_url = base_url

    def request(self, method, path, params=None, data=None, headers=None):
        request = f"{method} {path} HTTP/1.1\r\n"
        if headers is None:
            headers = {}
        for key, value in headers.items():
            request += f"{key}: {value}\r\n"
        request += "\r\n"
        if data is not None:
            request += data

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.base_url, 443))
        sock = ssl.wrap_socket(sock)
        sock.send(request.encode("utf-8"))

        response = b""
        while True:
            chunk = sock.recv(4096)
            if not chunk:
                break
            response += chunk

        status_code, headers, body = self._parse_response(response)

        return Response(status_code, headers, body)

    def _parse_response(self, response):
        lines = response.split(b"\r\n")

        status_line = lines[0].decode("utf-8")
        status_code = int(status_line.split()[1])

        headers = {}
        for line in lines[1:]:
            if not line:
                break
            key, value = line.decode("utf-8").split(": ", 1)
            headers[key] = value

        body = b"".join(lines[lines.index(b"") + 1:])

        return status_code, headers, body
