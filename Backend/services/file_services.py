import os
import hashlib

def calculate_checksum(filepath):
    """Calculate SHA-256 checksum of a file."""
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(8192):
            sha256_hash.update(chunk)
    return sha256_hash.hexdigest()

def save_chunk(socket, output_filename, chunk_size=512):
    """Save incoming file chunks from a socket."""
    with open(output_filename, 'wb') as f:
        while True:
            chunk = socket.recv(chunk_size)
            if not chunk:
                break
            f.write(chunk)

def serve_chunk(conn, filename, upload_folder, chunk_size=512):
    """Send a file in chunks to the client."""
    filepath = os.path.join(upload_folder, filename)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            while chunk := file.read(chunk_size):
                conn.sendall(chunk)
    else:
        conn.send(b'File not found')
