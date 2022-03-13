import socket

HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
PORT = 8080
HOST = "127.0.0.1"

encoding_format = 'utf-8'

def load(request):
    if(len(request) == 0):
        return (HDRS_404 + '404 Not Found.').encode(encoding_format)
    path = request.split(' ')[1]
    print("requested path: " + path)
    path = path[1:]
    print("requested path: " + path)
    try:
        with open(path, 'rb') as file:
            response = file.read()
        return HDRS.encode(encoding_format) + response
    except FileNotFoundError:
        return (HDRS_404 + '404 Not Found.').encode(encoding_format)

# http://127.0.0.1:8080/another.txt

if __name__ == '__main__':
    try:
        server = socket.create_server((HOST, PORT))
        server.listen(4)
        print("Server works . . .")
        while True:
            conn, address = server.accept()
            request = conn.recv(1024).decode(encoding_format)
            conn.send(load(request))
            conn.shutdown(socket.SHUT_WR)
    except KeyboardInterrupt:
        server.close()
        print('Server is closed.')