import socket
import os
import threading
from services.file_services import save_chunk, serve_chunk

class P2PNode:
    def __init__(self, host='localhost', port=6001):
        self.host = host
        self.port = port
        self.upload_folder = 'uploads/'  # Where the node stores its files

        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)

    def start_server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((self.host, self.port))
        server_socket.listen(5)
        print(f"Node listening on {self.host}:{self.port}")

        while True:
            conn, addr = server_socket.accept()
            print(f"Connection from {addr}")
            threading.Thread(target=self.handle_client, args=(conn,)).start()

    def handle_client(self, conn):
        try:
            filename = conn.recv(1024).decode('utf-8')
            serve_chunk(conn, filename, self.upload_folder)
        finally:
            conn.close()

    def request_file(self, peer_host, peer_port, filename):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((peer_host, peer_port))
        client_socket.send(filename.encode())

        save_chunk(client_socket, f'downloaded_{filename}')
        client_socket.close()

    def run(self):
        threading.Thread(target=self.start_server).start()

if __name__ == "__main__":
    node = P2PNode(host='localhost', port=6000)
    node.run()

    # Example to request a file from another peer
    node.request_file('localhost', 6001, 'example.txt')
