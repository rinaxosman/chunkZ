import socket
import os
import threading
import sys
from services.file_services import calculate_checksum, save_chunk, serve_chunk

class P2PNode:
    def __init__(self, host='localhost', port=6001):
        self.host = host
        self.port = port
        self.upload_folder = 'uploads/'  # Where the node stores its files

        if not os.path.exists(self.upload_folder):
            os.makedirs(self.upload_folder)

    def start_server(self):
        """Start the server to listen for incoming connections and handle file requests."""
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

            # Calculate the checksum of the file
            file_path = os.path.join(self.upload_folder, filename)
            checksum = calculate_checksum(file_path)
            print(f"Checksum of {filename} (to be sent): {checksum}")

            # Send the checksum first
            conn.sendall(checksum.encode())  # Send the checksum first

            # Send the file in chunks
            serve_chunk(conn, filename, self.upload_folder)
        finally:
            conn.close()

    def request_file(self, peer_host, peer_port, filename):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((peer_host, peer_port))

            # Send the filename request
            client_socket.send(filename.encode())

            # Receive the checksum first
            received_checksum = client_socket.recv(1024).decode('utf-8')
            print(f"Received checksum: {received_checksum}")

            # Save the file chunks
            downloaded_file = f'downloaded_{filename}'
            save_chunk(client_socket, downloaded_file)

            # Calculate the checksum of the received file
            calculated_checksum = calculate_checksum(downloaded_file)
            print(f"Calculated checksum of downloaded file: {calculated_checksum}")

            # Compare the checksums
            if received_checksum == calculated_checksum:
                print("File integrity verified! Transfer successful.")
            else:
                print("File corrupted. Checksums do not match!")

        except ConnectionRefusedError:
            print(f"Failed to connect to peer at {peer_host}:{peer_port}. Is the server running?")
        except FileNotFoundError:
            print(f"The file '{filename}' does not exist on the server.")
        finally:
            client_socket.close()


    def run(self):
        """Run the node server in a separate thread."""
        threading.Thread(target=self.start_server).start()


if __name__ == "__main__":
    # Get the port from the command-line argument or default to 6000
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 6000
    node = P2PNode(host='localhost', port=port)

    # Start the server in one thread
    node.run()

    # Optionally wait for the server to initialize
    import time
    time.sleep(2)  # Wait for 2 seconds to ensure the server is up

    # Example to request a file from another peer if the script is run with a filename
    if len(sys.argv) > 2:
        requested_file = sys.argv[2]
        node.request_file('localhost', 6001, requested_file)
