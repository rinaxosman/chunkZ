import os

def save_chunk(socket, output_filename):
    # Save incoming file in chunks
    with open(output_filename, 'wb') as f:
        while chunk := socket.recv(512):
            if not chunk:
                break
            f.write(chunk)
    print(f"File {output_filename} received successfully.")

def serve_chunk(conn, filename, upload_folder):
    # Serve the requested file in chunks
    filepath = os.path.join(upload_folder, filename)
    if os.path.exists(filepath):
        with open(filepath, 'rb') as file:
            while chunk := file.read(512):
                conn.sendall(chunk)
        print(f"File {filename} sent successfully.")
    else:
        print(f"File {filename} not found.")
        conn.send(b'File not found')
